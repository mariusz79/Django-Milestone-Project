from django.shortcuts import render, redirect
from posts.models import Post
from bugs.models import Bug
from features.models import Feature
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

# Create your views here.


def search(request):
    """ view to render the minimal search template """

    type_session = request.session.get('type', None)

    selections = ["bugs", "features", "posts"]
    search_type = request.GET.get('type')
    if search_type is None:
        search_type = type_session

    
    if request.GET['q'] == "":
        return redirect('search')


    if search_type == "bugs":
        posts = Bug.objects.filter(
        Q(tag__icontains=request.GET['q']) |
        Q(description__icontains=request.GET['q']) |
        Q(title__icontains=request.GET['q'])
        ).distinct().order_by('-id')
    if search_type == "features":
        posts = Feature.objects.filter(
        Q(tag__icontains=request.GET['q']) |
        Q(description__icontains=request.GET['q']) |
        Q(title__icontains=request.GET['q'])
        ).distinct().order_by('-id')
    if search_type == "posts":
        posts = Post.objects.filter(
        Q(tag__icontains=request.GET['q']) |
        Q(content__icontains=request.GET['q']) |
        Q(title__icontains=request.GET['q'])
        ).distinct().order_by('-id')



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

    return render(request, "search_results.html", context)

 


def search_results(request):
    """ view to render search results """

    context = {
        "selections": [
            "features",
            "bugs",
            "posts",
            ]
    }
    return render(request, "search.html", context)


