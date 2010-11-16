from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
import models

def index(request):
    news = models.SimpleNews.objects.filter(translations__language_code=request.LANGUAGE_CODE).order_by('-published')
    return render_to_response('cmsplugin_simplenews/index.html', {'news': news}, context_instance=RequestContext(request))

def view(request, id=None, slug=None):
    if id:
        kwargs = {'id': id, 'translations__language_code': request.LANGUAGE_CODE}
    elif slug:
        kwargs = {'slug_'+request.LANGUAGE_CODE: slug}
    else:
        from django.http import Http404
        raise Http404
    entry = get_object_or_404(models.SimpleNews, **kwargs)
    return render_to_response('cmsplugin_simplenews/view.html', {'entry': entry}, context_instance=RequestContext(request))