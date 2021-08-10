# Generated by Django 3.2.4 on 2021-06-26 18:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('job_type', models.CharField(choices=[('Remotly', 'Remotly'), ('Part Time', 'Part Time'), ('Internship', 'Internship'), ('Full Time', 'Full Time')], max_length=50)),
                ('Description', models.TextField(max_length=1000)),
                ('publishedAt', models.DateTimeField(auto_now=True)),
                ('Vacancy', models.IntegerField(default=1)),
                ('salary', models.IntegerField(default=0)),
                ('exp', models.IntegerField(default=1)),
                ('image', models.ImageField(default='media/default/job-offer-on-orange-note-260nw-752376046.jpg', upload_to='media/jobs/')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.category', verbose_name='Category Name')),
                ('employer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='job_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('protifolio', models.URLField()),
                ('cv', models.FileField(upload_to=job.models.cv_upload)),
                ('coverLetter', models.TextField(max_length=500)),
                ('applyAt', models.DateTimeField(auto_now=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('jobId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job', verbose_name='Job')),
            ],
        ),
    ]
