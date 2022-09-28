from django.db import models
import uuid


def file_upload(instance,filename):
		__,extention = getExtention(filename)
		return "media/%s.%s"%(instance.id,extention)

def getExtention(filename, ext=None):
	if ext:
		return filename, ext
	for c in range (len(filename)-1,0,-1):
		if filename[c] == ".":
			return filename[:c], filename[c:]
	return filename.split(".")



class File(models.Model):
	id 					= models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
	file 				= models.FileField(upload_to=file_upload, max_length=100)
	uploaded_at = models.DateTimeField(auto_now=True, auto_now_add=False)
	extension  	= models.CharField(max_length=50)

	def __str__(self):
			return str(self.id)
	
