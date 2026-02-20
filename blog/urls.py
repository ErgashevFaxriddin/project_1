from django.urls import path
from .views import bloglist

urlpatterns = [
    path('', bloglist, name='bloglist'),
]