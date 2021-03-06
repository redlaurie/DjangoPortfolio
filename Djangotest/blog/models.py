from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class PostTemplates(models.Model):
    templateURLS = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    Link = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE )
    image = models.ImageField(default='default.jpg', upload_to='project_pics')
    Template = models.ForeignKey(PostTemplates, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class postImages(models.Model):
    content = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='images')
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.post.title

