from django.shortcuts import redirect, render
from akun.models import pelanggan
from akun.forms import *
from bs_admin.models import barang, jasa, servis
from bs_admin.forms import FormLhtServis
from .decorators import pelanggan_area

@pelanggan_area
def index(request):
    context = {
        'judul' : 'Bali Soket Informindo',
        'heading' : 'Selamat Datang',
    }
    return render(request,'index.html',context)

@pelanggan_area
def servis_plg(request):
    srv = request.user.pelanggan.servis_set.all()
    
    context = {
        'judul' : 'Bali Soket Informindo',
        'heading' : 'Servis Saya',
        'srv' : srv,
    }
    return render(request,'data_servis.html',context)

@pelanggan_area
def lihat_servis(request, id_srv):
    srv = servis.objects.get(id=id_srv)
    if request.method == "POST":
        form = FormLhtServis(request.POST, instance=srv)
        if form.is_valid():
            form.save()
            return redirect('bs_admin:data_servis')
    else:
        form = FormLhtServis(instance=srv)

    context = {
        'judul' : 'Bali Soket Informindo',
        'heading' : 'Detail Servis',
        'form' : form,
    }

    return render(request, 'detail_servis.html', context)

@pelanggan_area
def brg_jasa_plg(request):

    brg = barang.objects.all()
    js = jasa.objects.all()

    context = {
        'judul' : 'Bali Soket Informindo',
        'heading' : 'Barang dan Jasa Servis',
        'brg': brg,
        'js': js,
    }
    return render(request,'data_barang_jasa.html',context)