# -*- encoding: utf-8 -*-
from myapp.tst_db import saffron_db
from myapp.models import Product, News, News_Opinion
from django.shortcuts import render, HttpResponse
import  datetime
# Create your views here.
def base_parent(request):

    return render(request, 'parent/base_parent.html')
"""========================================================="""
def best_news(request):
    list_news = News.objects.all()
    return render(request, 'news/best_news.html', {'list_news': list_news})
"""========================================================="""
def new_news(request):

    return render(request, 'news/new_news.html')
"""========================================================="""
def index_not_register(request):

    return render(request, 'index/index_not_register.html')
"""========================================================="""
def list_pro(request):
    products = Product.objects.all()
    #pro = products.Price_pro
    #print(pro)
    return render(request, 'shop/list_pro.html', {'list_pro': products})

"""========================================================="""
def plus_news(request):
    if request.method == 'GET':
        num = request.GET('plus')

"""========================================================="""
def buy_pro(request):
    if request.method == "POST":
        id_pro1 = request.POST.get('id_pro')
        much = request.POST.get('much')
        typ = request.POST.get('typ')
        #print id_pro1
        Object_pro = Product.objects.filter(id_pro=id_pro1)[0]
        Object_pro1 = Object_pro.Price_pro
        if typ == u"مثقال":
         final_price = int(much)*int(Object_pro1)
        elif typ == u"گرم":
            final_price = int(much)*int(Object_pro1)/4.7
        elif typ == u"کیلو":
            final_price = int(much)*int(Object_pro1)/4.7*1000
        #print final_price
        #print typ
        #print(Object_pro1)
        #print object_pro
        return  render(request, 'shop/buy_pro.html', {'list_pro': Object_pro, 'much': much, 'typ': typ, 'final_price': final_price})
"""========================================================="""
def insert_opinion(request, id1):
    if request.method == "POST":
        opinion1 = request.POST.get('opinion')
        print(opinion1)
        time_op = datetime.datetime.now()
        id_news = News.objects.filter(id=id1)
        print(id_news)
        Object_op = News_Opinion(id_news_id=id_news, Text_opinion=opinion1, Time_opinion=time_op, Num_opinion=1)
        Object_op.save()
        mess = u"تایید"
        return  render(request, 'news/best_news.html', {'mss': mess})
"""========================================================="""
def search_pro(request):
    if request.method == "POST":
        list_both = []
        if request.POST.get('Price_c') == '0':
            price_value = request.POST.get('price_s')
            list_price = Product.objects.filter(Price_pro=price_value)
            return render(request, 'shop/list_pro.html', {'list_pro': list_price})
        elif request.POST.get('name_c') == '0':
            name_value = request.POST.get('name_s')
            list_name = Product.objects.filter(Name_pro=name_value)
            return  render(request, 'shop/list_pro.html', {'list_pro': list_name})
        elif request.POST.get('price_c') == '0' and request.POST.get('name_c') == '0':
            list_both = Product.objects.filter(Name_pro=request.POST.get('name_s'), Price_pro=request.POST.get('price_s'))
    return  render(request, 'shop/list_pro.html', {'list_pro': list_both})
"""========================================================="""
def news_opinion(request):
    if request.method == "POST":
        news_op = request.POST.get('opinion')
        time_op = datetime.datetime.now()
        Object_op = News_Opinion(Text_opinion=news_op, Time_opinion=time_op, Num_opinion=1)
        Object_op.save()
        return HttpResponse(Object_op)







