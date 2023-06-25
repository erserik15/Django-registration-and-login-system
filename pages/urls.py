from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='pages-home'),
    path('about', about, name='pages-about'), 
    path('practice', practice_list, name='pages-practice_list'),
    path('practice/<practice_name>/', practice_detail, name='pages-practice_detail'),
    path('video_lessons_list', video_lessons_list, name='pages-video_lessons_list'),
    path('about_book', about_book, name='pages-about_book'),
]
