from django.shortcuts import render
from django.http import HttpResponse

def bloglist(request):
    html = f"""
    <h1>Blog page</h1><br>
    <h2>second</h2>

    <a href="/"> << First page </a>
    """
    return HttpResponse(html)