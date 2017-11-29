from django.conf.urls import include, url
from . import views

urlpatterns = [
    # url(r'^list/$', views.blog_list, name='blog_list'),
    # url(r'^article/(?P<pk>\d+)/$', views.blog_article, name='blog_article'),
    url(r'^lits/$', views.PageView.as_view(), name='page_list'),
    url(r'^title/(?P<title>.*)/$', views.PageDitailView.as_view(), name='blog_article'),
]