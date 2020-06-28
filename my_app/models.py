from django.db import models

# Create your models here.
class complain(models.Model):
    name= models.CharField(max_length=100)
    carname= models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Rating_CHOICES = (
    (1, 'Poor'),
    (2, 'Average'),
    (3, 'Good'),
    (4, 'Very Good'),
    (5, 'Excellent')
    )
    Rating = models.IntegerField(choices=Rating_CHOICES, default=1)
    message=models.CharField(max_length=500, blank=True)