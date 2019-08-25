from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature
from posts.models import Post
from django.utils import timezone

# Create your views here.
def index(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by('-published_date')[:3]
    return render(request, 'index.html', {'posts': posts})

def stats(request):
    """ view to render charts"""

    bugs_todo = Bug.objects.filter(status=1).count()
    bugs_doing = Bug.objects.filter(status=2).count()
    bugs_done = Bug.objects.filter(status=3).count()

    features_todo = Feature.objects.filter(status=1).count()
    features_doing = Feature.objects.filter(status=2).count()
    features_done = Feature.objects.filter(status=3).count()
    context = {
        'bugs_todo': bugs_todo,
        'bugs_doing': bugs_doing,
        'bugs_done': bugs_done,
        'features_todo': features_todo,
        'features_doing': features_doing,
        'features_done': features_done
    }

    return render(request, "stats.html", context)