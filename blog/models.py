from django.db import models

# Create your models here.
class Post(models.Model):
	title_blog = models.CharField(max_length = 20)
	data_blog = models.DateTimeField()
	text_blog = models.TextField(max_length = 300)
	image_blog = models.ImageField(upload_to = 'blog_images/')