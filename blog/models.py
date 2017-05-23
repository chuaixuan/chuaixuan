from django.db import models
from django.utils import timezone

class Shopping_list(models.Model):
    price = models.FloatField(max_length=200,name=False)
    classname = models.CharField(max_length=200,null=False)
    count= models.IntegerField(default=0)
    unit=models.CharField(max_length=200,null=False)
    name=models.CharField(max_length=200,null=False)
    def __str__(self):
        return self.name
class Purchased_goods(models.Model):
    price = models.FloatField(max_length=200, name=False)
    classname = models.CharField(max_length=200, null=False)
    count = models.IntegerField(default=0)
    unit = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=200, null=False)
    sumtotal=models.FloatField(default=0)
    original_price = models.FloatField(default=0)
    gift_count = models.IntegerField(default=0)
    gift_price = models.FloatField(default=0)
    def changed_count():
        total_count=0
        self=Purchased_goods.objects.all()
        for good in self:
            total_count+=good.count
        return total_count
    def total_price():
        total_price=0
        self=Purchased_goods.objects.all()
        for good in self:
            total_price+=good.original_price
        return total_price
    def total_gift_price():
        total_gift_price=0
        self=Purchased_goods.objects.all()
        for good in self:
            total_gift_price+=good.gift_count*good.price
        return total_gift_price

class GiftGoods(models.Model):
    classname = models.CharField(max_length=200, null=False);
    name = models.CharField(max_length=201, null=False);
    price = models.FloatField(max_length=200, null=False);
    unit = models.CharField(max_length=200, null=False);
    count = models.IntegerField(null=False, default=0);
    def __str__(self):
        return self.name