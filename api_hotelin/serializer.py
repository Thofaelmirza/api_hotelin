from rest_framework import serializers
from .models import karyawan,Produk,pesanan,pelanggan

class karyawanSerializer(serializers.ModelSerializer):
    class Meta:
        model = karyawan
        fields = '__all__'
    
class ProduktSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = '__all__'

class pesananSerializer(serializers.ModelSerializer):
    class Meta:
        model = pesanan
        fields = '__all__'

class pelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = pelanggan
        fields = '__all__'