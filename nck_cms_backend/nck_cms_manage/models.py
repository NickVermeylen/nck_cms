from django.db import models


# Create your models here.
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_heading = models.CharField(max_length=250)
    article_body = models.TextField()


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=250)
    customer_location_street = models.CharField(max_length=250)
    customer_location_postalCode = models.CharField(max_length=50)
    customer_location_municipality = models.CharField(max_length=250)
    customer_location_houseNumber = models.CharField(max_length=50)
    customer_location_extra = models.CharField(max_length=250, null=True)
    customer_description = models.TextField(null=True)




