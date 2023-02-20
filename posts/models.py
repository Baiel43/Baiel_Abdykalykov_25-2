from django.db import models


# Create your models here.


class Hashtag(models.Model):
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class Products(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=155)
    price = models.FloatField(default=0.00)
    description = models.TextField()
    rate = models.FloatField(default=0.0)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    def __str__(self):
        return self.title
