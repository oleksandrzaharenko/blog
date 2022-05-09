from django.db import models

# Create your models here.
class Event(models.Model):
	image_event = models.ImageField(upload_to = 'event_images/')
	text_event = models.CharField(max_length = 300)
