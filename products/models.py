from django.db import models

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    author = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name
    