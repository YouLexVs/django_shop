from django.db
import models

from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def short_description(self):
        return ' '.join(self.description.split()[:30])

    def __str__(self):
        return self.name