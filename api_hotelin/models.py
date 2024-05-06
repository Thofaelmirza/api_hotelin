from django.db import models
from django.utils import timezone


class karyawan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    tanggal_sewa = models.DateField()
    gaji = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama
    
class Produk(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    stok = models.PositiveIntegerField()

    def __str__(self):
        return self.nama
    
class pesanan(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    kuantias = models.PositiveIntegerField()
    dipesan_pada = models.DateTimeField(default=timezone.now)
    dikirim = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} - {self.produk.nama}"
    
class pelanggan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    alamat = models.TextField()
    nomor_hp = models.CharField(max_length=15)

    def __str__(self):
        return self.nama

