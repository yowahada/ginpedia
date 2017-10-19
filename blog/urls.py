from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='gin_list'),
	url(r'(?P<pk>\d+)/$', views.index, name='detail'),
]
