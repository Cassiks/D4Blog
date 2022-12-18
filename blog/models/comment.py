from django.db import models
from blog.models import WriteModel

class CommentsModel(models.Model):
    comments_author = models.CharField(max_length=35, blank=False, null=False)
    comments_email = models.CharField(max_length=100, blank=False, null=False)
    comments = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'
        verbose_name = "Comment"
        verbose_name_plural = "Comments"