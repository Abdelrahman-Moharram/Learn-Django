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

class Job(models.Model):
	
	title = models.CharField(max_length=50)
	
	job_type = models.CharField(max_length=50,choices = jobType)

	Description = models.TextField(max_length = 1000)

	publishedAt = models.DateTimeField(auto_now=True)

	Vacancy = models.IntegerField(default=1)

	salary = models.IntegerField(default=0)

	exp = models.IntegerField(default=1)

	cat = models.ForeignKey(Category,verbose_name = "Category Name", on_delete=models.CASCADE)


	def __str__(self):
	    return self.title
