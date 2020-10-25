from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.


def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s/%s/%s"%(instance.id,"jobImg",extension)

class job(models.Model):

    types=(
        ("Part Time", "Part Time"),
        ("Full Time", "Full Time")
    )
    owner        = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    name         = models.CharField(max_length=30)
    job_type     = models.CharField(max_length=20,choices=types)
    description  = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    salary       = models.IntegerField(null=False,blank=False)
    vacancy      = models.IntegerField(default=1)
    category     = models.ForeignKey('Category',on_delete=models.CASCADE)
    image        = models.ImageField(default='jobs/defaults/B612_20201021_094946_455.jpg',upload_to=image_upload)
    slug         = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(job,self).save(*args,**kwargs)

    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class apply(models.Model):
    job      = models.ForeignKey(job,related_name='apply_job', on_delete=models.CASCADE)
    name     = models.CharField(max_length=40)
    email    = models.EmailField(unique=True, max_length=254)
    website  = models.URLField(max_length=200)
    cv       = models.FileField(upload_to='jobs/cvs/', max_length=100)
    cover    = models.TextField(max_length=500)
    app_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    