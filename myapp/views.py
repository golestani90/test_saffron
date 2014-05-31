from myapp.tst_db import saffron_db
from myapp.models import Product
from django.shortcuts import render

# Create your views here.
def base_parent(request):

    return render(request, 'parent/base_parent.html')
"""========================================================="""
def best_news(request):

    return render(request, 'news/best_news.html')
"""========================================================="""
def new_news(request):

    return render(request, 'news/new_news.html')
"""========================================================="""
def index_not_register(request):

    return render(request, 'index/index_not_register.html')
"""========================================================="""
def list_pro(request):
    products = Product.objects.all()
    return render(request, 'shop/list_pro.html', {'list_pro': products})

"""========================================================="""
def plus_news(request):
    if request.method == 'GET':
        num = request.GET('plus')
"""========================================================="""
def buy_pro(request):
    if request.method == "POST":
        price1 = request.POST.get('price1')
        much = request.POST.get('much')
        typ = request.POST.get('typ')
        #print price1
        object_pro = Product.objects.filter(Price_pro=price1)
        #print object_pro
    return  render(request, 'shop/buy_pro.html', {'list_buy': object_pro, 'much': much, 'typ': typ})
"""========================================================="""







