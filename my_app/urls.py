from django.urls import path
from . import views

urlpatterns = [
    path('', views.first_view, name='first'),
    path('second/', views.second_view, name='second'),
    path('pages/<str:page>/', views.pages, name='pages'),
]
