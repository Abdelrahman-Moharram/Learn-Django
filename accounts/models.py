from django.db import models
from django.contrib.auth.models import User

usersTypes = {
 	('Employer','Employer'),
  	('Employee','Employee'),
}

def upload_image(instance,image):
        imageFile,extention = image.split(".")
        return "/media/users/imgs/%s/%s.%s"%(instance.id,instance.id,extention)
class userTips(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        userType = models.CharField(choices = usersTypes , max_length=20)
        userImage = models.ImageField(upload_to=upload_image,default='media/default/job-offer-on-orange-note-260nw-752376046.jpg')