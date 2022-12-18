# Generated by Django 4.1.4 on 2022-12-18 12:12

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_alter_categorymodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='WriteModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='ImgWrite')),
                ('title', models.CharField(max_length=30)),
                ('contents', models.TextField()),
                ('creatDate', models.DateField(auto_now_add=True)),
                ('date_of_issue', models.DateTimeField(auto_now=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writings', to=settings.AUTH_USER_MODEL)),
                ('categorys', models.ManyToManyField(related_name='write', to='blog.categorymodel')),
            ],
            options={
                'verbose_name': 'Write',
                'verbose_name_plural': 'Writings',
                'db_table': 'Write',
            },
        ),
    ]
