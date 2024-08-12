from django.db import models

# Create your models here.
class Salesrecord(models.Model):
    region = models.CharField(db_column="region", max_length=250,null=True,blank=True)
    country = models.CharField(db_column="country", max_length=50,null=True,blank=True)
    itemtype = models.CharField(db_column="itemtype", max_length=50,null=True,blank=True)
    saleschannel =models.CharField(db_column="saleschannel", max_length=50,null=True,blank=True)
    orderpriority = models.CharField(db_column="orderpriority", max_length=50,null=True,blank=True)
    orderdate = models.DateField(db_column="orderdate",  auto_now_add=False,null=True,blank=True)
    orderid = models.IntegerField(db_column="orderid",null=True,blank=True)
    shipdate = models.DateField(db_column="shipdate", auto_now_add=False,null=True,blank=True)
    unitssold = models.IntegerField(db_column="unitssold",null=True,blank=True)
    unitprice = models.FloatField(db_column="unitprice",null=True,blank=True)
    unitcost = models.FloatField(db_column="unitcost",null=True,blank=True)
    totalrevenue = models.FloatField(db_column="totalrevenue",null=True,blank=True,editable=False)
    totalcost = models.FloatField(db_column="totalcost",null=True,blank=True,editable=False)
    totalprofit = models.FloatField(db_column="totalprofit",null=True,blank=True,editable=False)

    class Meta:
        managed = False
        db_table = 'Salesrecord'
