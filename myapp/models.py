from django.db import models

# Create your models here.
class  Book(models.Model):
	subject=models.CharField(max_length = 100)
	author=models.CharField(max_length = 100)
	book=models.FileField(upload_to = '')
	book1=models.FileField(upload_to = '')
	book2=models.FileField(upload_to = '')
	book3=models.FileField(upload_to = '')
	book4=models.FileField(upload_to = '')
	book5=models.FileField(upload_to = '')
class Post(models.Model):
	subject=models.CharField(max_length = 100)
	author=models.CharField(max_length = 100)
	pdf1=models.FileField(upload_to = '')
	pdf2=models.FileField(upload_to = '')
	pdf3=models.FileField(upload_to = '')
	pdf4=models.FileField(upload_to = '')
	pdf5=models.FileField(upload_to = '')
	pdf6=models.FileField(upload_to = '')


	
	

          

	
