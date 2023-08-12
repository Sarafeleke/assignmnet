from django.db import models

# Create your models here.
class meetteam(models.Model):
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=200)
    postion= models.CharField(max_length=200)
    description = models.CharField(max_length=200)
class Abt_us(models.Model):
    about = models.CharField(max_length=800)
    image = models.ImageField(blank=True)
class Abt_us1(models.Model):
    title1 = models.CharField(max_length=200)
    description2 = models.CharField(max_length=200)
class Indexser(models.Model):
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=200)
    def __str__(self):
       return self.title
class CarouselItem(models.Model):
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=200)
    def __str__(self):
       return self.title
class whychoose(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    def __str__(self):
       return self.title
class Serivieinfo(models.Model):
   title = models.CharField(max_length=200)
   description = models.CharField(max_length=200)
   image = models.ImageField(blank=True)
   
   def __str__(self):
       return self.title
class ContactInformation(models.Model):
   
   address = models.CharField(max_length=200)
   email  = models.EmailField()
   phone = models.CharField(max_length=200)
  

   def __str__(self):
       return self.email
class ContactMessage(models.Model):
   name  = models.CharField(max_length = 200)
   email  =  models.EmailField()
   phone = models.CharField(max_length=200)
   subject  = models.CharField(max_length=200)
   message = models.TextField()
   
   def __str__(self):
      return self.name+"name"