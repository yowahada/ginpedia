from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import PostSitemap, PageSitemap, StaticViewSitemap

"""sitemap"""
sitemaps = {
    'post':PostSitemap,
    'page':PageSitemap,
    'static':StaticViewSitemap,
}

urlpatterns = [
    url(r'^list/$', views.GinListView.as_view(), name='gin_list'),

	url(r'^contact/$', views.contact_add, name='contact_add'),

    url(r'^about/$', views.about, name='about'),

    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),

    # URLを文字に、データ引渡しを手動で行う場合
    # url(r'^material/(?P<tag>.*)/$',views.MaterialsView.as_view(),name='Material'),

    url(r'^material/(?P<title>.*)/$',views.botanicalDetailView.as_view(),name='Material'),

    url(r'^$', views.TopListView.as_view(), name='post_list'),

    url(r'^sitemap\.xml$',sitemap, {
        'sitemaps':sitemaps,
        'template_name': 'custom_sitemap.xml',
    },name='sitemap'),
]

"""==============errorハンドラー==============
そのうち500書く
github:https://github.com/django/django/blob/master/django/views/defaults.py
=========================================="""
handler404 = 'main.views.error_404'