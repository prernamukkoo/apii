from django.db import models

# Create your models here.
from django.db import models

# class task(models.Model):
# 	title = models.CharField(max_length = 200)
# 	complete =models.BooleanField(default=False , blank=True, null=True)
# 	def __str__(self):
# 		return self.title


class Student(models.Model):
	name=models.CharField(max_length=50)
	friend=models.CharField(max_length=50)
	about=models.CharField(max_length=50)
	def __str__(self):
		return self.name