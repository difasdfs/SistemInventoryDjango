from django.db import models

# Create your models here.
class Produk(models.Model):
    CATEGORY = [
        ("DINE IN", "DINE IN"),
        ("GO FOOD", "GO FOOD"),
        ("GRABFOOD", "GRABFOOD"),
        ("MAKAN CREW", "MAKAN CREW"),
        ("SURPLUS", "SURPLUS"),
        ("TAKE AWAY", "TAKE AWAY"),
    ]

    no_sku = models.CharField(max_length=10)
    nama_produk = models.CharField(max_length=100)
    kategori = models.CharField(max_length=100, choices=CATEGORY)
    harga = models.IntegerField()

    def __str__(self):
        return self.no_sku + ' | ' + self.nama_produk + ' | ' + self.kategori

class AssemblyProduk(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    paper_cost_takeaway_l = models.IntegerField(default=0)
    paper_cost_takeaway_m = models.IntegerField(default=0)
    paper_cost_takeaway_paper_bag = models.IntegerField(default=0)
    paper_cost_dine_in_paper_tray = models.IntegerField(default=0)
    ayam_crispy = models.IntegerField(default=0)
    ayam_geprek_crispy = models.IntegerField(default=0)
    topping_crisbar = models.IntegerField(default=0)
    topping_saus_gravy = models.IntegerField(default=0)
    topping_matah = models.IntegerField(default=0)
    topping_mamah = models.IntegerField(default=0)
    topping_tomat = models.IntegerField(default=0)
    topping_manis = models.IntegerField(default=0)
    topping_goang = models.IntegerField(default=0)
    topping_keju = models.IntegerField(default=0)
    tahu_crispy = models.IntegerField(default=0)
    tempe_crispy = models.IntegerField(default=0)
    terong_crispy = models.IntegerField(default=0)
    telur_sayur = models.IntegerField(default=0)
    dua_chicken_skin_crispy = models.IntegerField(default=0)
    kol_crispy = models.IntegerField(default=0)
    kerupuk = models.IntegerField(default=0)
    sigulmer_manis_biscuit = models.IntegerField(default=0)
    perkedel = models.IntegerField(default=0)
    nasi_dine_in = models.IntegerField(default=0)
    es_teh_dine_in = models.IntegerField(default=0)
    lemon_tea_dine_in = models.IntegerField(default=0)
    milo_dine_in = models.IntegerField(default=0)
    orange_dine_in = models.IntegerField(default=0)
    nasi_takeaway = models.IntegerField(default=0)
    es_teh_takeaway = models.IntegerField(default=0)
    lemon_tea_takeaway = models.IntegerField(default=0)
    milo_takeaway = models.IntegerField(default=0)
    orange_takeaway = models.IntegerField(default=0)
    pudding_milo_dino = models.IntegerField(default=0)

    def __str__(self):
        return self.produk.no_sku + ' - ' + self.produk.nama_produk + ' - ' + self.produk.kategori

class BahanBaku(models.Model):
    no_sku = models.CharField(max_length=50)
    nama_bahan = models.CharField(max_length=100)

    def __str__(self):
        return self.no_sku + ' - ' + self.nama_bahan