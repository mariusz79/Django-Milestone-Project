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

