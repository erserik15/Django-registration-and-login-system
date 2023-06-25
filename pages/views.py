from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import os
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')


def practice_list(request):
    return render(request, 'pages/practice_list.html')

def practice_detail(request, practice_name = ''):
    path = os.path.join(settings.BASE_DIR, 'pages/templates/pages/practice_list', practice_name)
    if not os.path.exists(path):
        return HttpResponseNotFound("Not found: "+ practice_name + " with path: "+path)
    with open(path, 'r') as file:
        html_content = file.read()

    # Return the HTML response with UTF-8 encoding
    return HttpResponse(html_content, content_type='text/html; charset=utf-8')


def video_lessons_list(request):
    return render(request, 'pages/video_lessons_list.html')


def about_book(request):
    return render(request, 'pages/about_book.html')