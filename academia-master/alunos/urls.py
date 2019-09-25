from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^register/$', views.create_account, name='create_account'),
    url(r'^list/$', views.user_list, name='user_list'),
    url(r'^update/(?P<id>\d+)', views.user_update, name='user_update'),
    url(r'^ficha/(?P<id>\d+)', views.associate, name='associate'),
]