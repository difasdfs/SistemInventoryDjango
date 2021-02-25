from django.db import models

# Create your models here.
class Produk(models.Model):
    no_sku = models.CharField(max_length=10)
    nama_produk = models.CharField(max_length=100)

class AssemblyProduk(models.Model):
    paper_cost_takeaway_l = models.IntegerField()
    paper_cost_takeaway_m = models.IntegerField()
    paper_cost_takeaway_paper_bag = models.IntegerField()
    