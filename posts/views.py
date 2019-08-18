from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Post 
from .forms import BlogPostForm 
from django.contrib import auth, messages
from django.contrib.auth.models import User, Group
from django.contrib.admin.views.decorators import staff_member_required
from home.views import index


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
            return redirect(index)

    return render(request, 'blogpostform.html', {'form': form})

 
 

