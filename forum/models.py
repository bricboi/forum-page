from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    post = models.CharField(max_length=500, null=False, blank=False)
    upvote = models.BooleanField(null=False, blank=False, default=False)
    downvote = models.BooleanField(null=False, blank=False, default=False)


    def __str__(self):
        return self.title
