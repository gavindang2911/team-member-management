from django.db import models

role_choice = (
		('Admin', 'Admin'),
		('Regular Member', 'Regular Member'),
)
# Create your models here.
class Member(models.Model):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    email  = models.EmailField(max_length=70,blank=True)
    phone_number  = models.CharField(max_length=50,blank=True,null=True)
    role = models.CharField(max_length=50, blank=True, null=True, choices=role_choice, default='Regular Member')

    def __str__(self):
        return self.first_name
