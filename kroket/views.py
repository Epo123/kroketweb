from django.http import HttpResponse
from django.template import RequestContext, loader, Library

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
    if request.method == 'POST':

        cart = []

        article_names = request.POST.getlist('artname[]')
        article_quantities = request.POST.getlist('artquant[]')

        for index, article_name in enumerate(article_names):
            cart.append({
                'name': article_name,
                'quantity': article_quantities[index],
                'price': round(float(article_quantities[index]) * 9.9, 2)
            })

        test = request.POST.getlist('artname[]')
        artquant = request.POST.getlist('artquant[]')
    else:
        test = []
        artquant = []
        cart = []

    template = loader.get_template('afrekenen.html')

    context = RequestContext(request, {
        'test': test,
        'artquant': artquant,
        'cart': cart,
    })
    return HttpResponse(template.render(context))