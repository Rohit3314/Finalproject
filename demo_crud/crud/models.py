from django.db import models

class Customer(models.Model):
    cid = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=50)
    cemail = models.CharField(max_length=50)
    ccity = models.CharField(max_length=50)  
   
    class Meta:
        db_table = "tbl_customer" 
