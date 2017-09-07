from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^add_course', views.add, name = 'add'),
	url(r'^destroy/(?P<id>\d+)$', views.show_delete, name = 'show_delete'),
	url(r'^destroy/(?P<id>\d+)/delete/', views.destroy, name = 'delete')
]
