from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    return render(request, 'mUP_extra_app/index.html', {})

def log_in(request):
    if request.method =='GET':
        return render(request, 'mUP_extra_app/log.html', {'form': AuthenticationForm})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.success(request, "El usuario no existe, o la password es incorrecta")
            return render(request, 'mUP_extra_app/log.html', {'form': AuthenticationForm})
        else:
            login(request, user)
            return redirect('index')
        
@login_required
def log_out(request):
    logout(request)
    return redirect('index')  

@login_required
def soporte(request):
    return render(request, 'mUP_extra_app/soporte.html', {})


@login_required
def info(request):
    return render(request, 'mUP_extra_app/info.html', {})  



@login_required
def manual_maquina(request):
    return render(request, 'mUP_extra_app/manual_maquina.html', {})   

@login_required
def manual_vehiculo(request):
    return render(request, 'mUP_extra_app/manual_vehiculo.html', {})  

@login_required
def manual_area(request):
    return render(request, 'mUP_extra_app/manual_area.html', {})  

@login_required
def manual_repuesto(request):
    return render(request, 'mUP_extra_app/manual_repuesto.html', {})   

@login_required
def manual_pc(request):
    return render(request, 'mUP_extra_app/manual_pc.html', {})  

@login_required
def manual_herramienta(request):
    return render(request, 'mUP_extra_app/manual_herramienta.html', {})                        