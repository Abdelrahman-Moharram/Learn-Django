from django.db import models

jobType = {
	('Full Time','Full Time'),
	('Part Time','Part Time'),
	('Remotly','Remotly'),
	('Internship','Internship'),
}



class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
	    return self.name


def image_upload(instance,filename):
	image,extention = filename.split(".")
	return 'media/jobs/%s/%s.%s'%(instance.id,instance.id,extention)

class Job(models.Model):
	
	title = models.CharField(max_length=50)
	
	job_type = models.CharField(max_length=50,choices = jobType)

	Description = models.TextField(max_length = 1000)

	publishedAt = models.DateTimeField(auto_now=True)

	Vacancy = models.IntegerField(default=1)

	salary = models.IntegerField(default=0)

	exp = models.IntegerField(default=1)

	cat = models.ForeignKey(Category,verbose_name = "Category Name", on_delete=models.CASCADE)

	image = models.ImageField(upload_to=image_upload,default='media/default/job-offer-on-orange-note-260nw-752376046.jpg')

	def __str__(self):
	    return self.title
