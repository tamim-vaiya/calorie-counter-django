from django.db import models

# Create your models here.
class Food(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    carbs = models.FloatField()
    protein = models.FloatField()
    fats = models.FloatField()
    calories = models.IntegerField()
