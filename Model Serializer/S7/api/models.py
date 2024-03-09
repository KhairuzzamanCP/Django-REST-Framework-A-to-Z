from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 100)
    roll = models.IntegerField()
    city = models.CharField(max_length = 100)