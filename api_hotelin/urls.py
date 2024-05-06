from django.urls import path
from api_hotelin.views import karyawanlist,produklist,pesananlist,pelangganlist

urlpatterns = [
    path('karyawan/', karyawanlist.as_view()),
    path('produk/', produklist.as_view()),
    path('pesanan/', pesananlist.as_view()),
    path('pelanggan/', pelangganlist.as_view()),

]