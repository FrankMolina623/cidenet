from django.db import models

# Create your models here.
class Employee(models.Model):  
    firstLastname = models.CharField(max_length=20, null=True)
    secondLastname = models.CharField(max_length=20, null=True)
    firstName = models.CharField(max_length=20, null=True)
    otherName = models.CharField(max_length=50, null=True)
    contractCountry = models.CharField(max_length=50, null=True)
    id_type =  models.CharField(max_length=50, null=True)
    id_number = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=300, null=True)
    date_of_entry = models.DateField(null=True)
    company_area = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=50, default = 'Active', null=True)
    date_registered = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:  
        db_table = "employee"  
    
    def __str__(self):
        return self.firstName