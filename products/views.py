from django.shortcuts import HttpResponse, render, redirect
from datetime import datetime
from products.models import Products, Hashtag, Review
from products.forms import ReviewCreateform, ProductCreateForm


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
            'reviews': product.Reviews.all(),
            'form': ReviewCreateform
        }

        return render(request, 'products/detail.html', context=context)

    if request.method == 'POST':
        data = request.POST

        form = ReviewCreateform(data=data)
        product = Products.objects.get(id=id)

        if form.is_valid():
            Review.objects.create(
                text=form.cleaned_data.get('text'),
                product=product
            )

        context = {
            'product': product,
            'review': product.Reviews.all,
            'form': form
        }
        return render(request, 'products/detail.html', context=context)


def create_product_veiw(request):
    if request.method == 'GET':
        context = {
            'form': ProductCreateForm
        }
        return render(request, 'products/create.html', context=context)

    if request.method == 'POST':
        data, files = request.POST, request.FILES

        form = ProductCreateForm(data, files)

        if form.is_valid():
            Products.objects.create(
                image=form.cleaned_data.get('image'),
                title=form.cleaned_data.get('title'),
                price=form.cleaned_data.get('price'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate')
            )
            return redirect('/products')
        return render(request, 'products/create.html', context={
            "form": form
        })