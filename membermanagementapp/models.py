from django.db import models

# Create your models here.
class Member(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email  = models.EmailField(max_length=70,blank=True)
    phone_number  = models.CharField(max_length=50,blank=True,null=True)
    admin_role = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name
