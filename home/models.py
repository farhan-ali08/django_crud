from django.db import models

# Create your models here.

class contactus(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)

    class Meta:
        db_table = 'contactus'  # Custom table name
    
    def __str__(self):
        return self.name