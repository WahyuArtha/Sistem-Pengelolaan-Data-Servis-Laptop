"""sipds_bali_soket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teknisi/', include(('teknisi.urls', 'teknisi'), namespace='teknisi')),
    path('bs_admin/', include(('bs_admin.urls', 'bs_admin'), namespace='bs_admin')),
    path('', views.index, name='index'),
    path('akun/', include(('akun.urls', 'akun'), namespace='akun')),
    path('data_servis_saya/', views.servis_plg, name='servis_saya'),
    path('lihat_servis/<int:id_srv>',views.lihat_servis, name='lihat_servis'),
    path('barang_jasa_plg/', views.brg_jasa_plg, name='barang_dan_jasa'),
]
