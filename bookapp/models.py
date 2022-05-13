from turtle import title
from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    description=models.TextField()
    img=models.ImageField(blank=True)


    def imageURL(self):
        try:
            img=self.img.url
        except:
            img=''
        return img        
  


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])
        