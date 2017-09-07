from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
	url(r'^ninjas$', views.ninjas),
	url(r'^ninjas/(?P<color>[a-zA-Z]+)$', views.ninja),
	url(r'^goback$', views.reset)
]
