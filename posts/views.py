from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post, Like, Comment
from .forms import BlogPostForm, CommentForm
from django.contrib import auth, messages
from django.contrib.auth.models import User, Group
from django.contrib.admin.views.decorators import staff_member_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@login_required
@staff_member_required
def create_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    form = BlogPostForm()
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post_detail, post.pk)

    return render(request, 'blogpostform.html', {'form': form})

@login_required
@staff_member_required
def edit_post (request, pk=None):
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.user == post.author:
        if request.method == "POST":
            form = BlogPostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                post = form.save()
                return redirect(post_detail, post.pk)
        else:
            if request.user == post.author:
                form = BlogPostForm(instance=post)
    else:
        messages.success(request, "You need to be post author to edit it")
        return redirect(post_detail, post.pk)

    return render(request, 'blogpostform.html', {'form': form})


def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    # get post object
    post = get_object_or_404(Post, pk=pk)

    num_of_likes = post.likes
    post.views += 1
    post.save()

    #check if post is liked by user
    if request.user.is_authenticated():
        is_liked = Like.objects.filter(liked_post=pk, liker_user=request.user).exists()
    else:
        is_liked = False

    if request.method == "POST":
        form = CommentForm(data=request.POST)

        if form.is_valid():
            # create comment object but do not save to database
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.email = request.user.email
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            return redirect(post_detail, post.pk)
    else:
        comment_form = CommentForm()

    group = Group.objects.get(name="paid").user_set.all()

    return render(
        request, "postdetail.html", {
            'post': post,
            'num_of_likes': num_of_likes,
            'is_liked': is_liked,
            'comment_form': comment_form,
            'group': group
        })


@login_required
def liking(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #check if post is liked by user
    if request.user.is_authenticated():
        is_liked = Like.objects.filter(liked_post=pk,
                                       liker_user=request.user).exists()
    else:
        is_liked = False

    if not is_liked:
        post.likes += 1
        post.save()
        newlike = Like.objects.create(liker_user=request.user, liked_post=post)
    else:
        messages.success(request, "You can like only once")
        return redirect(post_detail, post.pk)
    return redirect(post_detail, post.pk)


def sort_by(request):
    """ view to render the minimal search template """

    type_session = request.session.get('type', None)

    selections = [
        "title az", "title za", "date up", "date down", "likes up",
        "likes down"
    ]
    search_type = request.GET.get('type')
    if search_type is None:
        search_type = type_session


    posts = Post.objects.all().order_by('-id')
    if search_type == "date up":
        posts = Post.objects.all().order_by('id')
    elif search_type == "date down":
        posts = Post.objects.all().order_by('-id')
    elif search_type == "title az":
        posts = Post.objects.all().order_by('title')
    elif search_type == "title za":
        posts = Post.objects.all().order_by('-title')
    elif search_type == "likes up":
        posts = Post.objects.all().order_by('likes')
    elif search_type == "likes down":
        posts = Post.objects.all().order_by('-likes')

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

    return render(request, "allposts.html", context)