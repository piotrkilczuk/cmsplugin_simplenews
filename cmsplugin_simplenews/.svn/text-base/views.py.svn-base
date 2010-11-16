from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
import models

def index(request):
    news = models.SimpleNews.objects.all().order_by('-published')
    return render_to_response('cmsplugin_simplenews/index.html', {'news': news}, context_instance=RequestContext(request))

def view(request, id=None, slug=None):
    if id:
        entry = get_object_or_404(models.SimpleNews, id=id)
    elif slug:
        entry = get_object_or_404(models.SimpleNews, slug=slug)
    else:
        from django.http import Http404
        raise Http404
    return render_to_response('cmsplugin_simplenews/view.html', {'entry': entry}, context_instance=RequestContext(request))