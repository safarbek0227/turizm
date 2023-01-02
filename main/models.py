from django.conf import settings
from django.db import models
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField


# Create your models here.
class MainPage(models.Model):
    img = models.ImageField(upload_to="MainImages%Y%m")
    title = models.CharField('title', max_length=250)
    content = RichTextField(max_length=305)
    def __str__(self):
        return "{}".format(self.title)
    
class Picture(models.Model):
    image = models.ImageField(upload_to="Pictures%Y%m")
    def __str__(self):
        return "{}".format(self.image)
    @property
    def image_url(self):
        return f"{settings.HOST}{self.image.url}" if self.image else ""

class Category(models.Model):
    title = models.CharField(max_length=125)
    slug = models.SlugField(max_length=125, unique=True)
    def __str__(self) :
        return '{}'.format(self.title)

class TravelTicket(models.Model):
    title = models.CharField(max_length=80)
    small_content = models.CharField(max_length=80)
    content = RichTextField()
    img = models.ManyToManyField(Picture)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    travel_hours = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return "{}".format(self.title)
        