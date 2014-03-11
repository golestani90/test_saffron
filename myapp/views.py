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




#ADMIN
"""=================================================================================================================================="""
def admin_parent(request):

    return render(request, 'parent/admin_parent.html')
"""========================================================="""
def admin_news_rss(request):

    return render(request, 'news/admin_news_rss.html')
"""========================================================="""
def admin_news_hand(request):

    return render(request,'news/admin_news_hand.html')