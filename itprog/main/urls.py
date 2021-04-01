from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login),
    path('data_schemas', views.data_schemas)

]
