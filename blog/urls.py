from django.urls import  path
from blog.views import bloglist

urlpatterns = [
    path('', bloglist, name='bloglist')
]