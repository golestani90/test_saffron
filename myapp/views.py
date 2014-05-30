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

    return render(request, 'shop/list_pro.html')

"""========================================================="""
def plus_news(request):
    if request.method == 'GET':
        num = request.GET('plus')







