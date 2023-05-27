from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    

class Category(models.Model):
    c_name = models.CharField(max_length=50,unique=True)
    def __str__(self):
        return self.name

class Product(models.Model):
    img = models.ImageField( upload_to='', height_field=None, width_field=None, max_length=None)
    P_name = models.CharField(max_length=200,unique=True)
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    def __str__(self):
        return self.P_name