from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length = 200)
    bookimage = models.ImageField(upload_to='images', blank=True)
    bookname = models.CharField(max_length = 200)
    bookauthor = models.CharField(max_length = 200)
    text = models.TextField()
    published_date = models.DateTimeField(default = timezone.now())

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs = {'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name = 'comments')
    author = models.CharField(max_length = 200)
    text = models.TextField()
    published_date = models.DateTimeField(default = timezone.now())

    def get_absolute_url(self):
        return reverse('post_list')

    def __stf__(self):
        return self.text
