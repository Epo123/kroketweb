from __future__ import print_function
from django.http import HttpResponse
from django.template import RequestContext, loader, Library
import pymysql

def index(request):
    besteld = ""
    if request.method == "POST":

        article_ids = request.POST.getlist('article_ids[]')

        besteld = "Uw bestelling is geplaatst!"

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='hahaha123', db='kroket')

        cur = conn.cursor()
        for article_id in article_ids:
            cur.execute("INSERT INTO bestelling (product_id,naam,adres,stad,telefoonnummer) VALUES ('"+article_id+"','"+request.POST['shipping_name']+"','"+request.POST['shipping_address']+"','"+request.POST['shipping_city']+"','"+request.POST['shipping_phonenumber']+"')")

        cur.close()
        conn.close()

    template = loader.get_template('index.html')

    context = RequestContext(request, {
        'besteld': besteld
    })
    return HttpResponse(template.render(context))

def assortiment(request):

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='hahaha123', db='kroket')

    cur = conn.cursor()

    cur.execute("SELECT id,omschrijving,voorraad,prijs FROM product")

    all_articles = cur

    cur.close()
    conn.close()

    template = loader.get_template('assortiment.html')

    context = RequestContext(request, {
        'all_articles': all_articles,
    })
    return HttpResponse(template.render(context))

def afrekenen(request):

    test = []
    artquant = []
    cart = []
    if request.method == 'POST':

        request.session['article_names'] = request.POST.getlist('artname[]')
        request.session['article_quantities'] = request.POST.getlist('artquant[]')
        request.session['article_price'] = request.POST.getlist('artprice[]')
        request.session['article_id'] = request.POST.getlist('artid[]')

        article_names = request.POST.getlist('artname[]')
        article_quantities = request.POST.getlist('artquant[]')
        article_price = request.POST.getlist('artprice[]')
        article_id = request.POST.getlist('artid[]')

        for index, article_name in enumerate(article_names):
            cart.append({
                'id': article_id[index],
                'name': article_name,
                'quantity': article_quantities[index],
                'price': article_price[index],
                'total_price': round(float(article_quantities[index]) * float(article_price[index]), 2)
            })
    else:

        if 'article_names' in request.session and 'article_quantities' in request.session:
            article_quantities = request.session['article_quantities']
            article_price = request.session['article_price']
            article_id = request.session['article_id']
            for index, article_name in enumerate(request.session['article_names']):
                cart.append({
                    'id': article_id[index],
                    'name': article_name,
                    'quantity': article_quantities[index],
                    'price': article_price[index],
                    'total_price': round(float(article_quantities[index]) * float(article_price[index]), 2)
                })


    template = loader.get_template('afrekenen.html')

    context = RequestContext(request, {
        'test': test,
        'artquant': artquant,
        'cart': cart,
    })
    return HttpResponse(template.render(context))