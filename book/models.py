from django.db import models
from django.utils import timezone

# Create your models here.
class Slam(models.Model):
	name = models.CharField(max_length=50)
	relationship = models.TextField()
	nick_name = models.CharField(max_length=50)
	like = models.CharField(max_length=266)
	dislike = models.CharField(max_length=266)
	message = models.CharField(max_length=266)
	gift = models.CharField(max_length=266)
	last_word= models.CharField(max_length=266)
	image = models.ImageField(upload_to="pics",null = False)
	video = models.FileField(upload_to='videos',null= True)

	def __str__(self):
		return self.name
