from django.db import models

class crudst(models.Model):
    stname = models.CharField(max_length=50)
    stemail = models.CharField(max_length=50)
    stnaddress = models.CharField(max_length=50)
    stmobile = models.IntegerField(max_length=50)
    stgender = models.CharField(max_length=1)
