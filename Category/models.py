from django.db import models
import random,string
from django.utils.text import slugify
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
def get_random_string(size):
    return ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = size))

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    slug=slugify(new_slug)
    Klass = instance
    qs_exists = Klass.objects.filter(slug=slug).exists()
    print(qs_exists)
    if qs_exists :
        new_slug = slugify(str(slug)+get_random_string(4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

class ListCategories(models.Model):
    
    name = models.CharField(max_length=100)
    icon = models.ImageField(blank=True)
    slug = models.SlugField(primary_key=True,blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(ListCategories,self.name)
        super(ListCategories, self).save(*args, **kwargs)


# class ListTags(models.Model):
#     menu = models.CharField(max_length=100)
#     slug = models.SlugField(primary_key=True,blank=True)
#     def __str__(self):
#         return self.menu
#     def save(self, *args):
#         if self.slug == '':
#             self.slug = unique_slug_generator(ListTags,self.menu)
#         super(ListTags, self).save(*args)

class List(models.Model):
    catgeory = models.ForeignKey(ListCategories,on_delete=models.CASCADE,related_name='subcategory')
    name = models.CharField(max_length=100)
    images = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    mobile = models.IntegerField(default=1)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)
    address = models.TextField(blank=True)
    price = models.IntegerField(default=1)
    # city = models.ForeignKey(Location,on_delete=models.CASCADE,blank=True, null=True,related_name='loc_name')
    contact_person = models.CharField(max_length=100,blank=True)
    contact_photo = models.ImageField(blank=True)
    menu = models.CharField(max_length=100,null=True, blank=True)
    location = models.CharField(max_length=100,null=True)
    slug = models.SlugField(primary_key=True,blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(List,self.name)
        super(List, self).save(*args, **kwargs)
TAGS_CHOICES = (
    ('BREAKFAST', 'BREAKFAST'),
     ('LUNCH', 'LUNCH'),
    ('DINNER', 'DINNER'),
  
)
class MenuItems(models.Model):
    # tags = models.ForeignKey(ListTags,on_delete=models.CASCADE,default=1,related_name='itemtags')
    menutags = models.CharField(max_length=100,choices=TAGS_CHOICES,default=1)
    items = models.CharField(max_length=100)
    
    restaurant = models.ForeignKey(List,on_delete=models.CASCADE,default=1,related_name='restaurantname')  
    price = models.PositiveIntegerField(default=1)
    slug = models.SlugField(primary_key=True,blank=True)
    def __str__(self):
        return self.items 
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = unique_slug_generator(MenuItems,self.items )
        super(MenuItems, self).save(*args, **kwargs)
# DAY_CHOICES = (
#     ('MONDAY', 'MONDAY'),
#     ('TUESDAY', 'TUESDAY'),
#     ('WEDNESDAY', 'WEDNESDAY'),
#     ('THURSDAY', 'THURSDAY'),
#     ('FRIDAY','FRIDAY'),
#     ('SATURDAY', 'SATURDAY'),
#     ('SUNDAY', 'SUNDAY')
# )
# class BusinessHours(models.Model):
#     day = models.CharField(max_length=100,choices=DAY_CHOICES,default=1)
#     time = models.TimeField(blank=True)
#     restaurant_name = models.ForeignKey(List,on_delete=models.CASCADE,related_name='hotel',default=1)
#     def __str__(self) -> str:
#         return str(self.restaurant_name)
class Features(models.Model):
    features_list = models.CharField(max_length=100,blank=True)
    hotelname = models.ForeignKey(List,on_delete=models.CASCADE,related_name='listname',default=1)
    def __str__(self) -> str:
        return str(self.hotelname)
RATING_CHOICES = (
        (5, '*****'),
        (4, '****'),
        (3, '***'),
        (2, '**'),
        (1, '*'),
    )
class reviews(models.Model):
    image = models.ImageField(blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    # subject = models.CharField(max_length=100)
    review_on = models.ForeignKey(List,on_delete=models.CASCADE,related_name='listreview',default=1)
    # comment = models.CharField(max_length=250)
    review = models.TextField(blank=True)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    slug = models.SlugField(blank=True)
    def __str__(self) -> str:
        return str(self.id)
    # image = models.ImageField(upload_to='media', null=True)
    # def __str__(self) -> str:
    #     return f"{self.name} ({self.product_name})"
    def save(self, *args, **kwargs):
        if self.id is None or self.slug is None or len(self.slug)==0:
            self.slug = unique_slug_generator(reviews,self.name)
        super().save()
TIMESLOT_LIST = (
        (0, '09:00 – 09:30'),
        (1, '10:00 – 10:30'),
        (2, '11:00 – 11:30'),
        (3, '12:00 – 12:30'),
        (4, '13:00 – 13:30'),
        (5, '14:00 – 14:30'),
        (6, '15:00 – 15:30'),
        (7, '16:00 – 16:30'),
        (8, '17:00 – 17:30'),
    )
class bookedlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    listbooked = models.ForeignKey(List,on_delete=models.CASCADE,related_name='bookedorder',null=True)
    date = models.DateField()
    time = models.IntegerField(choices=TIMESLOT_LIST)
    guests = models.IntegerField()
    booked_price = models.IntegerField(null=True)
    def __str__(self) -> str:
        return str(self.id)
class wishitems(models.Model):
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    wish_list = models.ForeignKey(List , on_delete = models.CASCADE)
    

    def __str__(self):
        return str(self.id)