from django.shortcuts import render
from .models import Usuario
from .models import Lead

def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'sobre/about.html')

def contato(request):
    return render(request,'contato/contato.html')

def usuariocad(request):
    return render(request,'cad/home.html')

def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    return render(request,'usuarios/usuarios.html',usuarios)

def leads(request):
    novo_lead = Lead()
    novo_lead.nome = request.POST.get('nome')
    novo_lead.email = request.POST.get('email')
    novo_lead.telefone = request.POST.get('telefone')
    novo_lead.assunto = request.POST.get('assunto')


    novo_lead.save()

    leads = {
        'leads': Lead.objects.all()
    }

    return render(request,'leads/leads.html',leads)