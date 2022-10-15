from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class data(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    message = models.CharField(max_length=5000)
    subject = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return str(self.user)