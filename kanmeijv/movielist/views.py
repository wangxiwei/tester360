from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Movie,HDTV,URLClicked
import datetime


class IndexView(generic.ListView):
    model = Movie
    template_name = 'movielist/index.html'
    context_object_name = 'movie_list'


class HDTVView(generic.ListView):
    model = HDTV
    template_name = 'movielist/hdtv.html'
    context_object_name = 'HDTV_list'


def save_url(request):
    movie_clicked = request.POST["movieName"]
    url_clicked = request.POST["movieUrl"]
    url_current = request.POST["currentUrl"]
    print movie_clicked,url_clicked,url_current,datetime.datetime.now()
    db=URLClicked(movie_clicked=movie_clicked,url_clicked=url_clicked, url_current=url_current, click_time=datetime.datetime.now())
    db.save()
    return HttpResponse("success")