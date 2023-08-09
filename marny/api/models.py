from django.db import models

# Create your models here.
class Lessons(models.Model):
    lessoncode = models.CharField(max_length=30, default="", unique="") 