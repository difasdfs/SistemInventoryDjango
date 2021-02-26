from django.contrib import admin
from .models import Produk, AssemblyProduk, BahanBaku

# Register your models here.
admin.site.register(Produk)
admin.site.register(AssemblyProduk)
admin.site.register(BahanBaku)