from .models import Produk

def masukin_data(isi):
    isi = isi.split(';')
    a = Produk(no_sku=isi[0], nama_produk=isi[1], kategori=isi[2], harga=int(isi[3]))
    a.save()
