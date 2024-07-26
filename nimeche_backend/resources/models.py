from django.db import models


# Create your models here.

class Material(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    file = models.FileField()
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
    
class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    media = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    