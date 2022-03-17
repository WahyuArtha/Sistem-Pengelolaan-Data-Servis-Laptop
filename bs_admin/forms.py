from django.forms import ModelForm
from django.forms import widgets
from django import forms
from akun.models import pegawai
from bs_admin.models import barang, jasa, servis, pembayaran
from datetime import date
#from random import randint
import random
import time

class FormTmhPgw(ModelForm):
    class Meta:
        model = pegawai
        fields = '__all__'

        labels = {
            'nama_pegawai':'Nama Pegawai',
            'alamat':'Alamat',
            'no_tlp':'No. Telepon/WA',
            'jabatan':'Jabatan',
        }

        widgets = {
            'nama_pegawai':forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Masukkan nama pegawai'}),
            'alamat':forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Masukkan alamat'}),
            'no_tlp':forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Masukkan no tlp'}),
            'jabatan':forms.Select(attrs= {'class':'form-control',}),
        }

class FormEdtPgw(ModelForm):
    class Meta:
        model = pegawai
        fields = '__all__'

        labels = {
            'nama_pegawai':'Nama Pegawai',
            'alamat':'Alamat',
            'no_tlp':'No. Telepon/WA',
            'jabatan':'Jabatan',
        }

        widgets = {
            'nama_pegawai':forms.TextInput(attrs= {'class':'form-control'}),
            'alamat':forms.TextInput(attrs= {'class':'form-control'}),
            'no_tlp':forms.TextInput(attrs= {'class':'form-control'}),
            'jabatan':forms.Select(attrs= {'class':'form-control'}),
        }

class FormBarang(ModelForm):
    class Meta:
        model = barang
        fields = '__all__'

        labels = {
            'nama_barang':'Nama Barang',
            'serialnomor':'Serial Nomor',
            'jenis_barang':'Jenis Barang',
            'harga_barang':'Harga Barang',
        }

        widgets = {
            'nama_barang':forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Masukkan nama barang'}),
            'serialnomor':forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Masukkan serial nomor'}),
            'jenis_barang':forms.Select(attrs= {'class':'form-control',}),
            'harga_barang':forms.NumberInput(attrs={'class':'form-control',}),
        }

class FormJasa(ModelForm):
    class Meta:
        model = jasa
        fields = '__all__'

        labels = {
            'nama_jasa':'Nama Jasa',
            'harga_jasa':'Harga Jasa',
        }

        widgets = {
            'nama_jasa':forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Masukkan nama jasa'}),
            'harga_jasa':forms.NumberInput(attrs={'class':'form-control',}),
        }

class FormTmhServis(ModelForm):
    class Meta:
        model = servis
        exclude = ['tgl_masuk', 'tgl_keluar']
        random.seed(time.perf_counter())
        tgl = date.today().strftime('%d%m%Y')
        noser = tgl + '-S0' + str(random.randint(1,100))

        labels = {
            'no_servis':'No Servis',
            'nama_barang_servis':'Nama Laptop',
            'serial_nomor':'Serial Nomor',
            'keluhan':'Keluhan',
            'kelengkapan':'Kelengkapan',
            'keterangan':'Keterangan',
            'status_servis':'Status Servis',
            'id_plg':'Pemilik',
        }

        widgets = {
            'no_servis':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly', 'value':noser}),
            'nama_barang_servis':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Masukkan Nama Laptop'}),
            'serial_nomor':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Masukkan Serial Nomor'}),
            'keluhan':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Masukkan Keluhan', 'rows':'3'}),
            'kelengkapan':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Masukkan Kelengkapannya'}),
            'keterangan':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Masukkan Keterangan', 'rows':'3'}),
            'status_servis':forms.Select(attrs= {'class':'form-control',}),
            'id_plg':forms.Select(attrs= {'class':'form-control',}),
        }

class FormEdtServis(ModelForm):
    class Meta:
        model = servis
        exclude = ['tgl_masuk', 'tgl_keluar']

        labels = {
            'no_servis':'No Servis',
            'nama_barang_servis':'Nama Laptop',
            'serial_nomor':'Serial Nomor',
            'keluhan':'Keluhan',
            'kelengkapan':'Kelengkapan',
            'keterangan':'Keterangan',
            'status_servis':'Status Servis',
            'id_plg':'Pemilik',
        }

        widgets = {
            'no_servis':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'nama_barang_servis':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'serial_nomor':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'keluhan':forms.Textarea(attrs={'class':'form-control', 'readonly':'readonly', 'rows':'3'}),
            'kelengkapan':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'keterangan':forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'status_servis':forms.Select(attrs= {'class':'form-control'}),
            'id_plg':forms.Select(attrs= {'class':'form-control', 'readonly':'readonly'}),
        }

class FormLhtServis(ModelForm):
    class Meta:
        model = servis
        exclude = ['tgl_masuk', 'tgl_keluar']

        labels = {
            'no_servis':'No Servis',
            'nama_barang_servis':'Nama Laptop',
            'serial_nomor':'Serial Nomor',
            'keluhan':'Keluhan',
            'kelengkapan':'Kelengkapan',
            'keterangan':'Keterangan',
            'status_servis':'Status Servis',
            'id_plg':'Pemilik',
        }

        widgets = {
            'no_servis':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'nama_barang_servis':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'serial_nomor':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'keluhan':forms.Textarea(attrs={'class':'form-control', 'readonly':'readonly', 'rows':'3'}),
            'kelengkapan':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'keterangan':forms.Textarea(attrs={'class':'form-control', 'rows':'3', 'readonly':'readonly'}),
            'status_servis':forms.Select(attrs= {'class':'form-control', 'readonly':'readonly'}),
            'id_plg':forms.Select(attrs= {'class':'form-control', 'readonly':'readonly'}),
        }

class FormTmhPmbyrn(ModelForm):
    class Meta:
        model = pembayaran
        exclude = ['total_bayar', 'id_jasa', 'id_barang']
        tgl = date.today().strftime('%d%m%Y')
        nopem = tgl + '-P0' + str(random.randint(1,100))

        labels = {
            'no_transaksi':'No Transaksi',
            'id_servis':'Nama Laptop',
            'id_plg':'Pemilik',
            'status_bayar':'Status Bayar',
        }

        widgets = {
            'no_transaksi':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly', 'value':nopem}),
            'id_servis':forms.Select(attrs={'class':'form-control',}),
            'id_plg':forms.Select(attrs={'class':'form-control',}),
            'status_bayar':forms.Select(attrs={'class':'form-control',}),
        }

class FormBayar(ModelForm):
    class Meta:
        model = pembayaran
        fields = '__all__'

        labels = {
            'no_transaksi':'No Transaksi',
            'id_servis':'Nama Laptop',
            'id_barang':'Nama Part',
            'id_jasa':'Nama Jasa',
            'id_plg':'Pemilik',
            'status_bayar':'Status Bayar',
        }

        widgets = {
            'no_transaksi':forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly',}),
            'id_servis':forms.Select(attrs={'class':'form-control', 'readonly':'readonly'}),
            'id_barang':forms.Select(attrs={'class':'form-control',}),
            'id_jasa':forms.Select(attrs={'class':'form-control', }),
            'id_plg':forms.Select(attrs={'class':'form-control', 'readonly':'readonly'}),
            'status_bayar':forms.Select(attrs={'class':'form-control',}),
            'total_bayar':forms.NumberInput(attrs={'class':'form-control', 'readonly':'readonly'}),
        }