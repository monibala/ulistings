from django.db import models
from django.contrib.auth.models import User

from Category.models import List
# Create your models here.
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
class order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    booked_list = models.ForeignKey(List,on_delete=models.CASCADE,related_name='listbooked',null=True)
    fname=models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField(null=True)
    # date = models.DateField()
    
    # time = models.TimeField()
    # guests = models.IntegerField()
    # def __str__(self):
    #     return self.user 
# class location(models.Model):
#     name = models.CharField(max_length=100)
#     images = models.ImageField(blank=True)
class contact_info(models.Model):
    name = models.CharField(max_length=100)
    mobile_number = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    subject = models.CharField(max_length=100)
    text = models.TextField(max_length=500)