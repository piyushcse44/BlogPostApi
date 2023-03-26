from django.db import models

# Create your models here.

class BlogContent(models.Model):
    id = models.IntegerField(unique=True,primary_key=True,editable=False)
    title = models.CharField(max_length=1000)
    content = models .TextField(null=True,blank=True)

    def __str__(self):
        return self.title
