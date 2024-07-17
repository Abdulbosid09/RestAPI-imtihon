from django.contrib import admin
from .models import Kurs,Dars,Izoh,LikeBosish,User


@admin.register(Kurs)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']
    list_editable = ['name']
    list_display_links = ['pk']


@admin.register(Dars)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'kurs', 'name', 'izoh', 'created_by','dars_videosi']
    list_editable = ['izoh']
    list_display_links = ['pk', 'name']


@admin.register(Izoh)
class LessonCommentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'dars', 'author', 'text']
    list_editable = ['text']
    list_display_links = ['pk', 'dars']

@admin.register(LikeBosish)
class LikeLessonAdmin(admin.ModelAdmin):
    list_display = ['pk', 'dars_like', 'like_or_dislike', 'author', 'created_by']
    list_display_links = ['pk', 'author']