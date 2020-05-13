from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('private', views.APIPrivate.as_view(), name='private'),
    path('role', views.SampleRole.as_view(), name='role'),
    path('permission', views.SamplePermission.as_view(), name='permission'),
    path('public', views.APIPublic.as_view(), name='public')
]