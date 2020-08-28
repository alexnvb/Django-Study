from django.contrib import admin
from django.utils.safestring import mark_safe

from django import forms
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget


# Register your models here.

class NewsAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm
    list_display = ('id', 'title', 'created_at', 'category', 'update_at', 'is_published', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('category', 'is_published')
    fields = ('title', 'content', 'photo', 'created_at', 'category', 'update_at', 'views', 'is_published', 'get_photo')
    readonly_fields = ('created_at', 'update_at', 'views', 'get_photo')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '---'

    get_photo.short_description = 'Mini Photo'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)