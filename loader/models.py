from django.db import models

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateTimeField()

    def __str__(self):
        return self.name