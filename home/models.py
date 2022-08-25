from django.db import models

# Create your models here.
class Cabin(models.Model):
    cabin_id = models.AutoField(primary_key=True)
    cabin_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cabin'


class Cookingcabin(models.Model):
    cookingcabin_id = models.AutoField(primary_key=True)
    cookingcabin_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CookingCabin'


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.TextField()
    item_desc = models.TextField(blank=True, null=True)
    item_price = models.IntegerField()
    item_category = models.TextField()
    item_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'Item'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    waiting_time = models.TextField(blank=True, null=True)
    order_status = models.TextField(blank=True, null=True)
    total_amount = models.TextField()  # This field type is a guess.
    cabin_id = models.IntegerField()
    cookingcabin_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Order'


class Transaction(models.Model):
    trans_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    amount = models.TextField()  # This field type is a guess.
    trans_status = models.TextField(blank=True, null=True)
    cabin_id = models.IntegerField()
    cookingcabin_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Transaction'