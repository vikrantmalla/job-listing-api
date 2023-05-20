from django.db import models

# Create your models here.
class Job(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='logos/')
    new = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    position = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    postedAt = models.DateTimeField()
    contract = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    languages = models.CharField(max_length=255)
    tools = models.CharField(max_length=255)

    def __str__(self):
        return self.position