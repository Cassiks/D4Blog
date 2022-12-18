from django.db import models
from autoslug import AutoSlugField
from blog.models import CategoryModel
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class WriteModel(models.Model):
    img = models.ImageField(upload_to='ImgWrite')
    title = models.CharField(max_length=30,blank=False, null=False)
    contents = RichTextField()
    creatDate = models.DateField(auto_now_add=True)
    date_of_issue = models.DateTimeField(auto_now=True)
    slug = AutoSlugField(populate_from = "title", unique=True)
    categorys = models.ManyToManyField(CategoryModel, related_name='write')
    author = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='writings')

    class Meta:
        verbose_name = "Write"
        verbose_name_plural = 'Writings'
        db_table = 'Write'