from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'saffron_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'myapp.views.base_parent', name='parent'),
    url(r'^best_news$', 'myapp.views.best_news', name='best'),
    url(r'^new_news$', 'myapp.views.new_news', name='new'),



    #"""======================================================================================================================="""
    #admin
    url(r'^admin_parent$', 'myapp.views.admin_parent', name='admin'),
    url(r'^admin_news_rss$', 'myapp.views.admin_news_rss', name='admin_news_rss'),
    url(r'^admin_news_hand$', 'myapp.views.admin_news_hand', name='admin_news_hand'),





)
