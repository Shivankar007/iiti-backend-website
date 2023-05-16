from django.db import models

# Create your models here.
class Books(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=5000)
    author = models.CharField(max_length=5000)
 
    def __str__(self) -> str:
        return self.name