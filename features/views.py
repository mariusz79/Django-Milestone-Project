from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from features.models import Feature, FeatureLike, FeatureComment
from features.forms import FeatureForm, FeatureCommentForm
from django.contrib import auth, messages
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
def create_feature(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    form = FeatureForm()
    if request.method == "POST":
        form = FeatureForm(request.POST, instance=feature)
        if form.is_valid():
            feature = form.save(commit=False)
            feature.author = request.user
            feature.save()
            return redirect(feature_detail, feature.pk)

    return render(request, 'featureform.html', {'form': form})


@login_required
def edit_feature(request, pk=None):
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.user == feature.author:
        if request.method == "POST":
            form = FeatureForm(request.POST, instance=feature)
            if form.is_valid():
                feature = form.save(commit=False)
                feature.author = request.user
                feature.save()
                return redirect(feature_detail, feature.pk)
        else:
            if request.user == feature.author:
                form = FeatureForm(instance=feature)
    else:
        messages.info(request, "You need to be feature author to edit it")
        return redirect(feature_detail, feature.pk)

    return render(request, 'featureform.html', {'form': form})


@login_required
def liking_feature(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    if feature.status != 4:
        #check if post is liked by user
        if request.user.is_authenticated():
            is_liked = FeatureLike.objects.filter(
                liked_feature=pk, liker_user=request.user).exists()
        else:
            is_liked = False

        if not is_liked:
            feature.likes += 1
            feature.save()
            newlike = FeatureLike.objects.create(liker_user=request.user,
                                             liked_feature=feature)
        else:
            messages.info(request, "You can like only once")
            return redirect(feature_detail, feature.pk)
    else:
        messages.info(request, "Likes are disabled for closed features")
        return redirect(feature_detail, feature.pk)
    return redirect(feature_detail, feature.pk)



def sort_features(request):
    """ view to render the minimal search template """

    type_session = request.session.get('type', None)

    selections = [
        "title az", "title za", "date up", "date down", "likes up",
        "likes down"
    ]
    search_type = request.GET.get('type')
    if search_type is None:
        search_type = type_session

    # searching with blank will still work. However, it will cause errors with
    # the pagination

    posts = Feature.objects.all().order_by('-id')
    if search_type == "date up":
        posts = Feature.objects.all().order_by('id')
    elif search_type == "date down":
        posts = Feature.objects.all().order_by('-id')
    elif search_type == "title az":
        posts = Feature.objects.all().order_by('title')
    elif search_type == "title za":
        posts = Feature.objects.all().order_by('-title')
    elif search_type == "likes up":
        posts = Feature.objects.all().order_by('likes')
    elif search_type == "likes down":
        posts = Feature.objects.all().order_by('-likes')

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 5)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        "object_list": posts,
        "selections": selections,
        "type": search_type
    }
    ordering = ['-id']

    request.session['type'] = search_type

    return render(request, "allfeatures.html", context)

def feature_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    # get post object

    feature = get_object_or_404(Feature, pk=pk) if pk else None

    num_of_likes = feature.likes
    feature.views += 1
    feature.save()

    #check if post is liked by user
    if request.user.is_authenticated():
        is_liked = FeatureLike.objects.filter(liked_feature=pk, liker_user=request.user).exists()
    else:
        is_liked = False

    if request.method == "POST":
        form = FeatureCommentForm(data=request.POST)

        if form.is_valid():
            # create comment object but do not save to database
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            # assign ship to the comment
            new_comment.Feature = Feature
            # save
            new_comment.save()
            return redirect(feature_detail, feature.pk)
    else:
        comment_form = FeatureCommentForm()

    group = Group.objects.get(name="paid").user_set.all()

    return render(
        request, "featuredetail.html", {
            'feature': feature,
            'num_of_likes': num_of_likes,
            'is_liked': is_liked,
            'comment_form': comment_form,
            'group': group
        })
