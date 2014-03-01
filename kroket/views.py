from django.http import HttpResponse
from django.template import RequestContext, loader

def index(request):
    template = loader.get_template('index.html')

    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))

def assortiment(request):
    template = loader.get_template('assortiment.html')

    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))

def afrekenen(request):
    template = loader.get_template('afrekenen.html')

    context = RequestContext(request, {

    })
    return HttpResponse(template.render(context))