from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_pelanggan:
                return redirect('index')
            else:
                return HttpResponse('Anda bukan pelanggan!')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

def unauthenticated_pgw(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_admin:
                return redirect('bs_admin:index')
            if request.user.is_teknisi:
                return redirect('teknisi:index')
            else:
                return HttpResponse('Anda tidak boleh pindah-pindah')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func