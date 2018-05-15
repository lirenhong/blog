from django.conf.urls import include, url
from django.contrib import admin
from blog_lrh.feeds import AllPostsRssFeed

urlpatterns = [
    # Examples:
    # url(r'^$', 'blogproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('blog_lrh.urls')),
    url(r'', include('comments.urls')),
    url(r'^all/rss/$', AllPostsRssFeed(), name='rss'),
]
