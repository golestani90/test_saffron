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







