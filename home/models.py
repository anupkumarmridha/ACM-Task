
from django.db import models
# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=125)
    email= models.CharField(max_length=125)
    phone= models.CharField(max_length=13)
    desc= models.TextField(max_length=125)
    #timeStamp=models.DateTimeField(auto_now_add=True, blank=False)
    timeStamp=models.DateTimeField()
    def __str__(self):
        return 'Message from ' + self.name + ' id-' + self.email

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title= models.CharField(max_length=125)
    content= models.TextField()
    author= models.CharField(max_length=13)
    slug= models.CharField(max_length=13)
    timeStamp=models.DateTimeField()
    def __str__(self):
        return self.title + ' by ' + self.author
