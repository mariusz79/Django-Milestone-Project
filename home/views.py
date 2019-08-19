from django.shortcuts import render
from bugs.models import Bug
from features.models import Feature

# Create your views here.
def index(request):
    return render(request, 'index.html')

def stats(request):
    """ view to render search results """


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