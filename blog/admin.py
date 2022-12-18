from django.contrib import admin
from blog.models import CategoryModel, WriteModel, CommentsModel

admin.site.register(CategoryModel)

class WriteAdmin(admin.ModelAdmin):
    search_fields = (
        'title', 'contents'
    )
    list_display = (
        'title', 'creatDate', 'date_of_issue'
    )

admin.site.register(WriteModel, WriteAdmin)

class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'comments_author', 'create_date', 'update_date'
    )
    search_fields = (
        'comments_author',
    )

admin.site.register(CommentsModel, CommentsAdmin)