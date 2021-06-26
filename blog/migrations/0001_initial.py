# Generated by Django 3.2.4 on 2021-06-26 18:28

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_image', models.ImageField(blank=True, null=True, upload_to=blog.models.post_image)),
                ('post_title', models.CharField(blank=True, max_length=150, null=True)),
                ('published_at', models.DateTimeField(auto_now=True)),
                ('post_Content', models.TextField(blank=True, max_length=2000, null=True)),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.usertips')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(blank=True, max_length=2000, null=True)),
                ('added_at', models.DateTimeField(auto_now=True)),
                ('comment_image', models.ImageField(blank=True, null=True, upload_to=blog.models.comment_image)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.usertips')),
            ],
        ),
    ]
