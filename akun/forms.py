from django.forms import ModelForm
from django.forms import widgets
from django import forms
from akun.models import LevelUser, pelanggan
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormTmhPlg(ModelForm):
    class Meta:
        model = pelanggan
        exclude = ['level_user']

        labels = {
            'nama_plg':'Nama Lengkap',
            'alamat':'Alamat',
            'no_tlp':'No. Telepon/WA',
        }

        widgets = {
            'nama_plg':forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Masukkan nama anda'}),
            'alamat':forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Masukkan alamat'}),
            'no_tlp':forms.TextInput(attrs= {'class':'form-control', 'placeholder':'Masukkan no tlp'}),
        }

class Registrasi(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'required':'',
            'name':'username',
            'id':'username',
            'type':'text',
            'class':'form-control',
            'placeholder':'Masukkan Username',
            'maxlength':'20',
        })
        self.fields["password1"].widget.attrs.update({
            'required':'',
            'name':'password1',
            'id':'password1',
            'type':'pasaword',
            'class':'form-control',
            'placeholder':'Masukkan Password',
            'maxlength':'20',
        })
        self.fields["password2"].widget.attrs.update({
            'required':'',
            'name':'password2',
            'id':'password2',
            'type':'password',
            'class':'form-control',
            'placeholder':'Masukkan Password kembali',
            'maxlength':'20',
        })

    class Meta:
        model = LevelUser
        fields = ['username', 'password1', 'password2']