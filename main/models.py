from django.conf import settings
from django.db import models
from django.utils import timezone


INTEGER_CHOICES= [tuple([x,x]) for x in range(1,10)]

class ContactMessage(models.Model):
    subject = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.subject + " from: " + self.name

class MerchOrder(models.Model):
    name = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    quanity= models.PositiveIntegerField()

    def __str__ (self):
        return self.subject + " from: " + self.name

class MerchItem(models.Model):
    item_line_one = models.CharField(max_length=200)
    item_line_two = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=200)
    description = models.TextField()

    def __str__ (self):
        return self.item_line_one + " " + self.item_line_two

class MerchFeature(models.Model):
    item_line_one = models.CharField(max_length=200)
    item_line_two = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.CharField(max_length=200)
    description_one = models.TextField()
    description_two = models.TextField()

    def __str__ (self):
        return self.item_line_one + " " + self.item_line_two
