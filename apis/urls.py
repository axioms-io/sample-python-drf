from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    path('private', views.Private.as_view(), name='private'),
    path('admin', views.Admin.as_view(), name='admin'),
    path('public', views.Public.as_view(), name='public')
]