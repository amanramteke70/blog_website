from django.db import models
from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    message = models.CharField(max_length=400)

class Blognews(models.Model):
    tittle = models.CharField(max_length=80)
    des = HTMLField()
    img = models.ImageField(upload_to='news/images', default="")

    slug = AutoSlugField(populate_from='tittle',unique=True,null=True, default=None)