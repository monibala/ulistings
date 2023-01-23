from django.db import models

from Category.models import unique_slug_generator

# Create your models here.
class bloginfo(models.Model):
    images = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    date = models.DateField()
    posted_by = models.CharField(max_length=100)
    slug = models.SlugField(primary_key=True,blank=True)
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(bloginfo,self.title)
        super(bloginfo, self).save(*args, **kwargs)