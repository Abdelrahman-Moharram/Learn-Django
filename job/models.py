from django.db import models
from django.utils.text import slugify
import accounts.models

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s/%s/%s"%(instance.id,"jobImg",extension)



class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class job(models.Model):

    types=(
        ("Part Time", "Part Time"),
        ("Full Time", "Full Time")
    )
    owner        = models.ForeignKey("accounts.account",related_name='job_owner',on_delete=models.CASCADE,error_messages={"required":"you should login first"})
    name         = models.CharField(max_length=30,error_messages={"required":"you shoould enter valid name"})
    job_type     = models.CharField(max_length=20,choices=types,error_messages={"required":"Can't be Null"})
    description  = models.TextField(max_length=1000,error_messages={"required":"enter valid message to get people like job require"})
    published_at = models.DateTimeField(auto_now=True)
    salary       = models.IntegerField(null=False,blank=False,error_messages={"required":"required salary"})
    vacancy      = models.IntegerField(default=1)
    category     = models.ForeignKey(Category,on_delete=models.CASCADE,error_messages={"required":"you should add categry"})
    image        = models.ImageField(default='jobs/defaults/B612_20201021_094946_455.jpg',upload_to=image_upload)
    slug         = models.SlugField(null=True,blank=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.name)
        super(job,self).save(*args,**kwargs)

    
    def __str__(self):
        return self.name




class apply(models.Model):
    job      = models.ForeignKey(job,related_name='apply_job', on_delete=models.CASCADE)
    name     = models.CharField(max_length=40,error_messages={"required":"Enter a Valid name"})
    email    = models.EmailField(unique=True, max_length=254,error_messages={"required":"Enter a Valid Email"})
    website  = models.URLField(max_length=200,error_messages={"required":"Enter a Valid website"})
    cv       = models.FileField(upload_to='jobs/cvs/', max_length=100,error_messages={"required":"upload your cv"})
    cover    = models.TextField(max_length=500,error_messages={"required":"enter message to get hired"})
    app_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    