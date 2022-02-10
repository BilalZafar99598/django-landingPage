from django.db import models

# Create your models here.

class Brand(models.Model):
    Brand=models.CharField(max_length=200)
    Brand_Image=models.ImageField(upload_to='media/Brands')
    day_left = models.IntegerField()


    class Meta:
        db_table="Brand"
    def __str__(self):
        return self.Brand


class Product(models.Model):
    Product_name=models.CharField(max_length=200)
    Product_Brand=models.ForeignKey(Brand,on_delete=models.CASCADE ,default=1)
    Product_Image=models.ImageField(upload_to='media/Products')
    Product_Disription=models.CharField(max_length=1000)
    Stock=models.IntegerField(max_length=5000)
    class Meta:
        db_table='Products'

    def __str__(self):
        return self.Product_name

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products_by_Brandid(Brand_id):
        if Brand_id:
            return Product.objects.filter(Product_Brand=Brand_id)
        else:
            return Product.get_all_products();