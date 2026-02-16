from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def bloglist(request):
    posts = Post.objects.all()
    post_list = ""
    for post in posts:
        post_list += f"<li>{post}</li>"
    return HttpResponse(f"<ul>{post_list}</ul>")
