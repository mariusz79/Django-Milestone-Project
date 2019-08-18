from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Bug, BugLike, BugComment
from .forms import BugForm, BugCommentForm
from django.views.generic import ListView
from django.contrib import auth, messages
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def create_bug(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    form = BugForm()
    if request.method == "POST":
        form = BugForm(request.POST,instance=bug)
        if form.is_valid():
            bug = form.save(commit=False)
            bug.author = request.user
            bug.save()
             
            return redirect(bug_detail, bug.pk)

    return render(request, 'bugform.html', {'form': form})
def bug_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    # get post object

    bug = get_object_or_404(Bug, pk=pk) if pk else None

    num_of_likes = bug.likes
    bug.views += 1
    bug.save()

    #check if post is liked by user
    if request.user.is_authenticated():
        is_liked = BugLike.objects.filter(liked_bug=pk, liker_user=request.user).exists()
    else:
        is_liked = False

    if request.method == "POST":
        form = BugCommentForm(data=request.POST)

        if form.is_valid():
            # create comment object but do not save to database
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            # assign ship to the comment
            new_comment.bug = bug
            # save
            new_comment.save()
            return redirect(bug_detail, bug.pk)
    else:
        comment_form = BugCommentForm()

    group = Group.objects.get(name="paid").user_set.all()

    return render(
        request, "bugdetail.html", {
            'bug': bug,
            'num_of_likes': num_of_likes,
            'is_liked': is_liked,
            'comment_form': comment_form,
            'group': group,
        })

        
@login_required
def edit_bug(request, pk=None):
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.user == bug.author:
        if request.method == "POST":
            form = BugForm(request.POST, instance=bug)
            if form.is_valid():
                bug = form.save()
                return redirect(bug_detail, bug.pk)
        else:
            if request.user == bug.author:
                form = BugForm(instance=bug)
    else:
        messages.info(request, "You need to be bug author to edit it")
        return redirect(bug_detail, bug.pk)

    return render(request, 'bugform.html', {'form': form})

@login_required
def liking_bug(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    if bug.status != 4:
        #check if post is liked by user
        if request.user.is_authenticated():
            is_liked = BugLike.objects.filter(liked_bug=pk,
                                        liker_user=request.user).exists()
        else:
            is_liked = False

        if not is_liked:
            bug.likes += 1
            bug.save()
            newlike = BugLike.objects.create(liker_user=request.user, liked_bug=bug)
        else:
            messages.info(request, "You can like only once")
            return redirect(bug_detail, bug.pk)
    else:
        messages.info(request, "Likes are disabled for closed bugs")
        return redirect(bug_detail, bug.pk)
    return redirect(bug_detail, bug.pk)
