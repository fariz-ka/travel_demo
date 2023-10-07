from django.db import models


# Create your models here.
class place(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='pic')
    Dis = models.TextField()

    def __str__(self):
        return self.name


class team(models.Model):
    img = models.ImageField(upload_to='pic')
    name = models.CharField(max_length=250)
    discri = models.TextField()

    def __str__(self):
        return self.name
