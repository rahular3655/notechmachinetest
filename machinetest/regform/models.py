from django.db import models

# Create your models here.



class form(models.Model):
    name=models.CharField(max_length=50,null=True)
    mailid=models.EmailField(null=True)
    password=models.CharField(max_length=50,null=True)
    phonenumber=models.CharField(max_length=12,null=True)
    
    def __str__(self):
        return self.name