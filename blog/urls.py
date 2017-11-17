from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^list/$', views.post_list, name='gin_list'),

	url(r'^contact/$', views.contact_add, name='contact_add'),

    url(r'^about/$', views.about, name='about'),

    url(r'^(?P<pk>\d+)/$', views.detail, name='detail'),


    # URLを文字に、データ引渡しを手動で行う場合
    # url(r'^material/(?P<tag>.*)/$',views.MaterialsView.as_view(),name='Material'),

    url(r'^material/(?P<title>.*)/$',views.botanicalDetailView.as_view(),name='Material'),

    url(r'^lists/$', views.GinListView.as_view(), name='post_list'),
]
"""==============errorハンドラー==============
そのうち500書く
github:https://github.com/django/django/blob/master/django/views/defaults.py
=========================================="""
handler404 = 'main.views.error_404'