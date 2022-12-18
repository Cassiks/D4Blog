from django.contrib import admin
from blog.models import CategoryModel, WriteModel

admin.site.register(CategoryModel)
admin.site.register(WriteModel)