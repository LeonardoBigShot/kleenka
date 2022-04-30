from django import template
from django.shortcuts import get_object_or_404, render
from django.template import context, loader
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    paginator = Paginator(products, 30)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    
    return render(request, 'index.html',
                    {
                        'category': category,
                        'categories': categories,
                        'products': products,
                        'page_obj': page_obj
                    })


def delivery(request):
    category = None
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'delivery.html', context)


def order(request):
    category = None
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'order.html', context)


def support(request):
    category = None
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, 'support.html', context)


def by_category(request, category_slug):
    products = Product.objects.order_by('-created')
    categories = Category.objects.all()
    current_category = Category.objects.get(pk=category_slug)
    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        products = paginator.page(paginator.num_pages)
    context = {'products': products, 'categories': categories,
               'current_category': current_category, 'page_obj': page_obj}
    return render(request, 'category.html', context)

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'card.html', {'product': product,
                    'cart_product_form': cart_product_form})
