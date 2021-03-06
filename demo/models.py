from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, help_text='Select the Author')
    BLOG_CATEGORY = (
        ('GOT','GOT'),
        ('Suits', 'Suits'),
        ('Dark', 'Dark'),
        ('Breaking Bad','Breaking Bad'),
        ('Money Heist', 'Money Heist'),
    )
    category = models.CharField(max_length=20, choices = BLOG_CATEGORY, default = 'Null')
    title = models.CharField(max_length = 200, help_text = 'Enter title', unique=True)
    text = models.TextField(help_text = 'Enter text')
    created_date = models.DateTimeField(default = timezone.now,)
    published_date = models.DateTimeField(null = True, blank = True)
    reference = models.URLField(help_text='Enter the reference to your Blog Post', blank=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        unique_together = ("author", "title")   
        # "unique_together" will make sure that the author and the title of the post remains unique, while entering the data.
        # here, if the same user(author) tries to post a blog with the same title it'll give an error

class Comment(models.Model):
    post = models.ForeignKey('demo.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now, blank=True)
    approved_comment = models.BooleanField(default=False, blank=True)

    def approve(self):
        self.approved_comment = True
        self.save()
    
    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)