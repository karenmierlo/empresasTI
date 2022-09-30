from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


# @login_required
def index(request):

    data = "Versao 0.21 - apresentação"
    

    return render(request, 'index.html', 
        { 'dados' : data } 
    )

# @login_required
def db1(request):

    data = "Versao 0.01 - Dashboard 1 (um) "

    return render(request, 'dashboard1.html', 
        { 'dados' : data } 
    )    

# @login_required
def db2(request):

    data = "Versao 0.01 - Dashboard 2 (dois)"
    

    return render(request, 'dashboard2.html', 
        { 'dados' : data } 
    )        


# @login_required
def about(request):
    data = "Nos da equipe xxxxxx trabalhamos intensamente em bla bla bla" 

    return render(request, 'about.html', 
        { 'dados' : data } 
    )  

def karen(request):
    data = "Meu nome é Karen, eu tenho 26 anos" 

    return render(request, 'karen.html', 
        { 'dados' : data } 
    )  

