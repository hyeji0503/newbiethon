from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=200)
    radio = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Review2(models.Model):
    title2 = models.CharField(max_length=200)
    radio2 = models.CharField(max_length=200)
    writer2 = models.CharField(max_length=100)
    description2 = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
 
 
class Review3(models.Model):
    title3 = models.CharField(max_length=200)
    radio3 = models.CharField(max_length=200)
    writer3 = models.CharField(max_length=100)
    description3 = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   