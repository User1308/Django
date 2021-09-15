from django.db import models
from django.shortcuts import redirect, reverse
from django.urls import reverse_lazy
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class Book(models.Model):

    name = models.CharField(max_length=200)
    slug = models.SlugField()
    author = models.CharField(max_length=200)
    uploaded_by = models.ForeignKey('User', on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to='images/')
    category = models.ForeignKey('Category',null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} by {self.author}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'slug': self.slug})

class Chapter(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    completed = models.BooleanField()
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class User(AbstractUser):
    email = models.EmailField(_('Email Address'), unique=True)

    def __str__(self):
        return self.username

class PreferredCategories(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
