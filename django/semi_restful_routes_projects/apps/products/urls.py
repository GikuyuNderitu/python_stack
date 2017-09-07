from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.to_index, name='to_index'),
    url(r'^products$', views.index, name='index'),
	url(r'^products/show/(?P<id>\d+)$', views.show, name='show'),
	url(r'^products/new$', views.new, name = 'add'),
	url(r'^products/create$', views.create, name = 'create'),
	url(r'^products/edit/(?P<id>\d+)$', views.edit, name = 'edit'),
	url(r'^products/update/(?P<id>\d+)$', views.update, name = 'update'),
	url(r'^products/delete/(?P<id>\d+)$', views.destroy, name = 'delete')
]
