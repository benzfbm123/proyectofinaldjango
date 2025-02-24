from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def login_personalizado(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('lista_servidores')  
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'cuentas/login.html')

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
def logout_personalizado(request):
    
    logout(request)
    return redirect('login')
def inicio(request):
    return redirect('login')

