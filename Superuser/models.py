from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class ad_profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='admin_record')
    name=models.CharField(max_length=30,)
    email = models.EmailField()
    img=models.ImageField(blank=True,null=True)
    dob = models.DateField(blank=True,null=True)
    mobile = models.IntegerField(blank=True,null=True)
    about = models.TextField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    designation = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.name