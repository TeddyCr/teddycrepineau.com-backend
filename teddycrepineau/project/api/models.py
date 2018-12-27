from django.db import models
from django.contrib.auth.models import User
from  django.contrib.postgres.fields import ArrayField

class Posts(models.Model):
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=100)
    content = models.TextField()
    tags = ArrayField(
            models.CharField(max_length=20, blank=True
            , help_text="Enter a tag related to your post"),
            size=4,
           )
    creation_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class meta:
        db_table = 'posts'

# Create your models here.
