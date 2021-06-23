from django.db import models
from django.contrib.auth.models import User

usersTypes = {
 	('Employer','Employer'),
  	('Employee','Employee'),
}

def image_upload(instance,filename):
        imageFile,extention = filename.split(".")
        return "media/users/%s/%s.%s"%(instance.user,instance.user,extention)
class userTips(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        userType = models.CharField(choices = usersTypes , max_length=20)
        userImage = models.ImageField(upload_to=image_upload,default='media/default/job-offer-on-orange-note-260nw-752376046.jpg')