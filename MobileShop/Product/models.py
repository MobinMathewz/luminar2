from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length= 300)
    mobilenum = models.IntegerField(max_length=15)
    emailid = models.CharField(unique=True,max_length=150)
    username = models.CharField(unique=True,max_length=150)
    password = models.CharField(max_length=150)
    isActive = models.ImageField(max_length=2)
    def __str__(self):
        return self.name

class Category(models.Model):
    category_name = models.CharField(unique=True,max_length=120)
    def __str__(self):
        return self.category_name

class Color(models.Model):
    color_name = models.CharField(unique=True,max_length=120)
    def __str__(self):
        return self.color_name

class Brand(models.Model):
    brand_name = models.CharField(unique=True,max_length=150)
    def __str__(self):
        return self.brand_name

class Product(models.Model):
    product_name= models.CharField(max_length=150)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price= models.IntegerField(max_length=100)
    quantity= models.IntegerField(max_length=150)
    color= models.ForeignKey(Color,on_delete=models.CASCADE)
    ram= models.CharField(max_length=150)
    product_code = models.CharField(unique=True, max_length=120)
    brand= models.ForeignKey(Brand,on_delete=models.CASCADE)
    def __str__(self):
        return self.product_name+self.product_code

class Order(models.Model):
    product_code= models.ForeignKey(Product,on_delete=models.CASCADE)
    userid= models.ForeignKey(Users,on_delete=models.CASCADE)
    date= models.DateTimeField()
    def __str__(self):
        return self.product_code+self.userid