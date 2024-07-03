from django.urls import path
from message import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adushi-page/', views.adushi, name='adushi')
]