from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    instrument = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name} - {self.instrument}"
    
