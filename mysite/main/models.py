from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True, blank=True)
    git = models.URLField(max_length=900, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


class Contact(models.Model):
    message = models.TextField()
    email = models.EmailField(max_length=500)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}'s message"
    



