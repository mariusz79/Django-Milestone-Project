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