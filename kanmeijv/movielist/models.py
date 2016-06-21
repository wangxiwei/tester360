# encoding=utf-8
from __future__ import unicode_literals

from django.db import models


class Movie(models.Model):
    movie_name = models.CharField(max_length=500)
    movie_url = models.CharField(max_length=1000)
    movie_state = models.CharField(max_length=50)
    movie_update = models.CharField(max_length=50)
    movie_return = models.CharField(max_length=50)
    movie_countdown = models.CharField(max_length=50)

    def __unicode__(self):
        return self.movie_name


class HDTV(models.Model):
    tv_name = models.CharField(max_length=500)
    tv_url = models.CharField(max_length=1000)
    tv_download = models.CharField(max_length=2000)
    tv_size = models.CharField(max_length=50)
    tv_format = models.CharField(max_length=50)
    tv_sub = models.CharField(max_length=2000)

    def __unicode__(self):
        return self.tv_name


class URLClicked(models.Model):
    movie_clicked = models.CharField(max_length=100)
    url_clicked = models.CharField(max_length=1000)
    url_current = models.CharField(max_length=1000)
    click_time = models.CharField(max_length=100)

    def __unicode__(self):
        return self.movie_clicked