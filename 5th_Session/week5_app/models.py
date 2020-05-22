from django.db import models

class youtube(models.Model):
    ch_name = models.CharField(max_length=30)
    cre_name = models.CharField(max_length=30)
    prefer = models.IntegerField()
    live = models.BooleanField(max_length=5)
    sub_num = models.IntegerField()
    link_1 = models.TextField(max_length=500)
    link_2 = models.TextField(max_length=500)
    link_3 = models.TextField(max_length=500)