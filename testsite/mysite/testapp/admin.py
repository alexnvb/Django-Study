from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from .models import *

# Register your models here.

admin.site.register(Rubric, MPTTModelAdmin)
admin.site.register(Article)