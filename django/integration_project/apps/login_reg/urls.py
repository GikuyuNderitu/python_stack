from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),
	url(r'^logout$', views.logout, name = 'logout'),
	url(r'^login$', views.login, name = 'login'),
	url(r'^register$', views.register, name = 'register'),
	url(r'^edit$', views.show_edit, name = 'show_edit'),
	url(r'^edit/(?P<id>\d+)$', views.edit, name = 'edit'),
	url(r'^courses_users/$', views.show_courses, name = 'show_courses'),
	url(r'^courses_users/process$', views.match_user_course, name = 'match')
]
