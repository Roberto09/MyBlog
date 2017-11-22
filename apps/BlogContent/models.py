from django.db import models
from datetime import datetime 

#Needed to install pillow for the ImageField

# Create your models here.
class BlogPost(models.Model):
	title=models.CharField(max_length=50)
	content1=models.TextField()
	image1=models.ImageField(upload_to='Blog_Images', blank=True)
	content2=models.TextField(blank=True, null=True)
	image2=models.ImageField(upload_to='Blog_Images', blank=True)
	ref_code=models.TextField(blank=True, null=True)
	github_link=models.TextField(blank=True, null=True)
	references=models.TextField(blank=True, null=True)
	upload_date=models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.title
#bold stuff in css font-weight: bold;

