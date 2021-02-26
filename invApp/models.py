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
    paper_cost_takeaway_l = models.IntegerField()
    paper_cost_takeaway_m = models.IntegerField()
    paper_cost_takeaway_paper_bag = models.IntegerField()
    paper_cost_dine_in_paper_tray = models.IntegerField()
    ayam_crispy = models.IntegerField()
    ayam_geprek_crispy = models.IntegerField()
    topping_crisbar = models.IntegerField()
    topping_saus_gravy = models.IntegerField()
    topping_matah = models.IntegerField()
    topping_mamah = models.IntegerField()
    topping_tomat = models.IntegerField()
    topping_manis = models.IntegerField()
    topping_goang = models.IntegerField()
    topping_keju = models.IntegerField()
    tahu_crispy = models.IntegerField()
    tempe_crispy = models.IntegerField()
    terong_crispy = models.IntegerField()
    telur_sayur = models.IntegerField()
    dua_chicken_skin_crispy = models.IntegerField()
    kol_crispy = models.IntegerField()
    kerupuk = models.IntegerField()
    sigulmer_manis_biscuit = models.IntegerField()
    perkedel = models.IntegerField()
    nasi_dine_in = models.IntegerField()
    es_teh_dine_in = models.IntegerField()
    lemon_tea_dine_in = models.IntegerField()
    milo_dine_in = models.IntegerField()
    orange_dine_in = models.IntegerField()
    nasi_takeaway = models.IntegerField()
    es_teh_takeaway = models.IntegerField()
    lemon_tea_takeaway = models.IntegerField()
    milo_takeaway = models.IntegerField()
    orange_takeaway = models.IntegerField()
    pudding_milo_dino = models.IntegerField()

    def __str__(self):
        return self.produk.no_sku + ' - ' + self.produk.nama_produk + ' - ' + self.produk.kategori

class BahanBaku(models.Model):
    no_sku = models.CharField(max_length=50)
    nama_bahan = models.CharField(max_length=100)

    def __str__(self):
        return self.no_sku + ' - ' + self.nama_bahan