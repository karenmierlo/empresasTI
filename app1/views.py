from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


# @login_required
def index(request):

    data = " "
    

    return render(request, 'index.html', 
        { 'dados' : data } 
    )

def home(request):

    data = " "

    return render(request, 'home.html', 
        { 'dados' : data } 
    )    

# @login_required
def alunos(request):

    data = " "

    return render(request, 'alunos.html', 
        { 'dados' : data } 
    )    

# @login_required
def empresas(request):
    data = " " 

    return render(request, 'empresas.html', 
        { 'dados' : data } 
    )  

def beneficios(request):
    data = " " 

    return render(request, 'beneficios.html', 
        { 'dados' : data } 
    )  

def sobrenos(request):
    data = " " 

    return render(request, 'sobrenos.html', 
        { 'dados' : data } 
    )  
