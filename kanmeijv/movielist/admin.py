from django.contrib import admin
from .models import Movie,HDTV,URLClicked


class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_name','movie_state','movie_update','movie_return','movie_countdown')
    list_filter = ['movie_update']
    search_fields = ['movie_name']

admin.site.register(Movie,MovieAdmin)


class HDTVAdmin(admin.ModelAdmin):
    list_display = ('tv_name','tv_size','tv_format')
    search_fields = ['tv_name']

admin.site.register(HDTV,HDTVAdmin)


class URLClickedAdmin(admin.ModelAdmin):
    list_display = ('movie_clicked','url_clicked','url_current','click_time')
    search_fields = ['movie_clicked']
    list_filter = ['click_time']

admin.site.register(URLClicked,URLClickedAdmin)