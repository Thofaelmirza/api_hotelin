from rest_framework import generics
from api_hotelin.serializer import karyawanSerializer,ProduktSerializer,pesananSerializer,pelangganSerializer
from api_hotelin.models import karyawan,Produk,pesanan,pelanggan

class karyawanlist(generics.ListCreateAPIView):
    queryset = karyawan.objects.all()
    serializer_class = karyawanSerializer

class produklist(generics.ListCreateAPIView):
    queryset = Produk.objects.all()
    serializer_class = ProduktSerializer

class pesananlist(generics.ListCreateAPIView):
    queryset = pesanan.objects.all()
    serializer_class = pesananSerializer

class pelangganlist(generics.ListCreateAPIView):
    queryset = pelanggan.objects.all()
    serializer_class = pelangganSerializer

