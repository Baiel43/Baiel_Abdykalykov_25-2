from django.shortcuts import HttpResponse, render
from datetime import datetime
from products.models import Products, Hashtag


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my project')


def now_date(request):
    if request.method == 'GET':
        return HttpResponse(datetime.now())


def goodby(request):
    if request.method == 'GET':
        return HttpResponse('Goodby User!')


def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def hashtags(request):
    if request.method == 'GET':
        Hashtags = Hashtag.objects.all()
        context = {
            'Hashtags': Hashtags
        }
        return render(request, 'hashtag/Hashtags.html', context=context)


def products_view(request):
    if request.method == 'GET':
        products = Products.objects.all()

        context = {
            'products': [
                {
                    'id': product.id,
                    'title': product.title,
                    'price': product.price,
                    'rate': product.rate,
                    'image': product.image,
                    'hashtags': product.hashtags.all()
                }
                for product in products
            ]
        }

        return render(request, 'products/products.html', context=context)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Products.objects.get(id=id)

        context = {
            'product': product,
            'reviews': product.Reviews.all()
        }

        return render(request, 'products/detail.html', context=context)