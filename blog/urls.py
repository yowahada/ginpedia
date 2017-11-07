from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^list/$', views.post_list, name='gin_list'),
	url(r'^contact/$', views.contact_add, name='contact_add'),
    url(r'^about/$', views.about, name='about'),
    url(r'(?P<pk>\d+)/$', views.detail, name='detail'),
]

#errorハンドラー。そのうち500書く
#github:https://github.com/django/django/blob/master/django/views/defaults.py
handler404 = 'main.views.error_404'