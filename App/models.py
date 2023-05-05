from django.db import models

# Create your models here.
class Design(models.Model):
    name=models.CharField(max_length=30,null=True,default="image",blank=True)
    img=models.ImageField(upload_to='pics/',null=True,blank=True)
    desc=models.TextField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name
  

class Product(models.Model):
    product_name=models.CharField(max_length=30)
    product_description=models.TextField()
    product_image=models.ImageField(upload_to='pics/',null=True,blank=True)
    trending_product=models.BooleanField(default=False)
    product_kg=models.IntegerField(null=True,blank=True,default=0)
    product_cost=models.IntegerField(null=True,blank=True,default=0)
     
    

class Order(models.Model):
    customer_name=models.CharField(max_length=30,editable=False)
    customer_number=models.IntegerField(editable=False)
    products=models.TextField()
    total_number_of_product=models.IntegerField(default=1)
    total_cost=models.IntegerField()
    time=models.CharField(max_length=30,default="",editable=False)
    status=models.BooleanField(default=False)

    

class Feedback(models.Model):
    fname=models.CharField(max_length=30,editable=False)
    fnumber=models.IntegerField(editable=False)
    feedback=models.TextField(editable=False)
    fstatus=models.BooleanField(default=False)




