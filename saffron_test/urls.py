from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'saffron_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myapp.views.base_parent', name='parent'),
    url(r'^best/news$', 'myapp.views.best_news', name='best'),
    url(r'^new/news$', 'myapp.views.new_news', name='new'),
    url(r'^index/not_register$', 'myapp.views.index_not_register', name='not_register'),
    url(r'^plus/news$', 'myapp.views.plus_news', name='plus'),
    url(r'^list/pro$', 'myapp.views.list_pro', name='list_pro'),
    url(r'^buy/pro$', 'myapp.views.buy_pro', name='buy_pro'),
    #url(r'^insert/opinion/([^/]+)$', 'myapp.views.insert_opinion', name='insert_opinion'),
    url(r'^search/pro$', 'myapp.views.search_pro', name='search_pro'),
    url(r'^news/opinion$', 'myapp.views.news_opinion', name='news_opinion'),












)
