from django.conf import settings
from django.db import models
from django.utils import timezone


INTEGER_CHOICES= [tuple([x,x]) for x in range(1,10)]

#forms

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
        return self.item + " from: " + self.name

class MerchItem(models.Model):
    item_line_one = models.CharField(max_length=200)
    item_line_two = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    description = models.TextField()

    def __str__ (self):
        return self.item_line_one + " " + self.item_line_two

class MerchFeature(models.Model):
    item_line_one = models.CharField(max_length=200)
    item_line_two = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    mobile_image = models.CharField(max_length=200)
    description_one = models.TextField()
    description_two = models.TextField()

    def __str__ (self):
        return self.item_line_one + " " + self.item_line_two

#settings

class HomeSettings(models.Model):
    edit_name = models.CharField(max_length=200)
    banner_pic = models.CharField(max_length=200)
    bio = models.TextField()
    background_color = models.CharField(max_length=200)
    text_color = models.CharField(max_length=200)
    button_color = models.CharField(max_length=200)
    button_text_color = models.CharField(max_length=200)
    pic_one = models.CharField(max_length=200)
    pic_two = models.CharField(max_length=200)
    pic_three = models.CharField(max_length=200)
    video_link = models.CharField(max_length=200)

    def __str__ (self):
        return self.edit_name

class PortfolioSettings(models.Model):
    edit_name = models.CharField(max_length=200)
    production_one = models.CharField(max_length=200)
    production_two = models.CharField(max_length=200)
    production_three = models.CharField(max_length=200)
    mixing_one = models.CharField(max_length=200)
    mixing_two = models.CharField(max_length=200)
    mixing_three = models.CharField(max_length=200)
    features_one = models.CharField(max_length=200)
    features_two = models.CharField(max_length=200)
    features_three = models.CharField(max_length=200)

    def __str__ (self):
        return self.edit_name
