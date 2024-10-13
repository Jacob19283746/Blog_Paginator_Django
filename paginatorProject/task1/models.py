from django.db import models
from django.forms import CharField, EmailField

class Author(models.Model):
    username = models.CharField(max_length=20, default='Jacob')
    email = models.EmailField(blank=True, null=True)

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


