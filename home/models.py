from django.db import models

from tinymce import models as tinymce_models

# Create your models here.
class Story(models.Model):
    title=models.CharField(max_length=255)
    role=models.CharField(max_length=255, blank=True, null=True)
    period=models.CharField(max_length=255, blank=True, null=True)
    location=models.CharField(max_length=255, blank=True, null=True)
    description=tinymce_models.HTMLField()
    image=models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
