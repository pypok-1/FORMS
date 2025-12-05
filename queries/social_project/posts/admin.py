from django.contrib import admin
from .models import Post, Profile, Comment, Category, Tag   # добавь Tag в импорт

admin.site.register(Tag)