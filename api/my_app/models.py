from django.db import models

# Create your models here.
class Snippet(models.Model):
    GENDER_CHOICES=(
        ('Male','MALE'),
        ('Female','FEMALE'),
        )
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    gender=models.CharField(max_length=255, choices=GENDER_CHOICES, default='Male')

    class Meta:
        ordering = ['-id']
