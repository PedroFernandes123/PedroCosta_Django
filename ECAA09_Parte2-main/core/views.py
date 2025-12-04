from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import ClienteSignUpForm, ProblemaForm, OficinaPerfilForm, OficinaSignUpForm
from .models import Problema, User, PerfilOficina, Interesse

def home(request):
    if request.user.is_authenticated:
        if request.user.is_cliente:
            return redirect('dashboard_cliente')
        elif request.user.is_oficina:
            return redirect('dashboard_oficina')
    return render(request, 'core/home.html')

def signup(request):
    """View para escolher o tipo de cadastro (Cliente ou Oficina)"""
    return render(request, 'registration/signup_choice.html')

def signup_cliente(request):
    if request.method == 'POST':
        form = ClienteSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard_cliente')
    else:
        form = ClienteSignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'tipo': 'Cliente', 'is_cliente': True})

def signup_oficina(request):
    if request.method == 'POST':
        form = OficinaSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard_oficina')
    else:
        form = OficinaSignUpForm()
    return render(request, 'registration/signup.html', {'form': form, 'tipo': 'Oficina', 'is_oficina': True})

@login_required
def dashboard_cliente(request):
    problemas = Problema.objects.filter(cliente=request.user).order_by('-data_criacao')
    if request.method == 'POST':
        form = ProblemaForm(request.POST, request.FILES)
        if form.is_valid():
            problema = form.save(commit=False)
            problema.cliente = request.user
            problema.save()
            return redirect('dashboard_cliente')
    else:
        form = ProblemaForm()
    return render(request, 'core/dashboard_cliente.html', {'problemas': problemas, 'form': form})

@login_required
def dashboard_oficina(request):
    # Listar problemas em aberto (sem oficina atribuída)
    problemas_abertos = Problema.objects.filter(status='ABERTO')
    
    # Listar problemas que a oficina manifestou interesse
    # (excluindo os que já pegou ou que foram rejeitados)
    problemas_selecionados = Problema.objects.filter(
        interesses__oficina=request.user,
        interesses__status='INTERESSADA',
        oficina__isnull=True  # Ainda não tem oficina definida
    ).distinct().order_by('-interesses__data_interesse')
    
    # Listar problemas que a oficina está trabalhando
    meus_servicos = Problema.objects.filter(oficina=request.user).order_by('-data_criacao')
    
    return render(request, 'core/dashboard_oficina.html', {
        'problemas_abertos': problemas_abertos,
        'problemas_selecionados': problemas_selecionados,
        'meus_servicos': meus_servicos
    })

@login_required
def pegar_servico(request, pk):
    problema = get_object_or_404(Problema, pk=pk)
    if not problema.oficina and request.user.is_oficina:
        problema.oficina = request.user
        problema.status = 'ANDAMENTO'
        problema.save()
    return redirect('dashboard_oficina')

@login_required
def concluir_servico(request, pk):
    problema = get_object_or_404(Problema, pk=pk)
    if problema.oficina == request.user:
        problema.status = 'CONCLUIDO'
        problema.save()
    return redirect('dashboard_oficina')

@login_required
def aceitar_interesse(request, interesse_id):
    """Aceita o interesse de uma oficina em um problema"""
    interesse = get_object_or_404(Interesse, pk=interesse_id)
    
    # Verificar se o usuário é o cliente do problema
    if interesse.problema.cliente == request.user:
        # Rejeitar todos os outros interesses
        interesse.problema.interesses.exclude(pk=interesse.id).update(status='REJEITADA')
        
        # Aceitar este interesse
        interesse.status = 'INTERESSADA'
        interesse.problema.oficina = interesse.oficina
        interesse.problema.status = 'ANDAMENTO'
        
        interesse.save()
        interesse.problema.save()
    
    return redirect('dashboard_cliente')

@login_required
def rejeitar_interesse(request, interesse_id):
    """Rejeita o interesse de uma oficina em um problema"""
    interesse = get_object_or_404(Interesse, pk=interesse_id)
    
    # Verificar se o usuário é o cliente do problema
    if interesse.problema.cliente == request.user:
        interesse.status = 'REJEITADA'
        interesse.save()
    
    return redirect('dashboard_cliente')

@login_required
def manifestar_interesse(request, problema_id):
    """Oficina manifesta interesse em um problema"""
    problema = get_object_or_404(Problema, pk=problema_id)
    
    # Verificar se o usuário é uma oficina
    if not request.user.is_oficina:
        return redirect('dashboard_cliente')
    
    # Verificar se já existe interesse
    interesse, created = Interesse.objects.get_or_create(
        problema=problema,
        oficina=request.user,
        defaults={'status': 'INTERESSADA'}
    )
    
    if request.method == 'POST' and 'mensagem' in request.POST:
        interesse.mensagem = request.POST.get('mensagem', '')
        interesse.save()
    
    return redirect('dashboard_oficina')

@login_required
def detalhe_problema(request, problema_id):
    """Exibe detalhes de um problema específico"""
    problema = get_object_or_404(Problema, pk=problema_id)
    
    # Verificar permissão
    # Apenas o cliente pode ver seus problemas
    # Ou qualquer oficina pode ver problemas em aberto
    if request.user.is_cliente and problema.cliente != request.user:
        # Cliente tentando ver problema de outro
        return redirect('dashboard_cliente')
    
    # Pegar interesse desta oficina (se houver)
    meu_interesse = None
    if request.user.is_oficina:
        try:
            meu_interesse = Interesse.objects.get(problema=problema, oficina=request.user)
        except Interesse.DoesNotExist:
            pass
    
    context = {
        'problema': problema,
        'meu_interesse': meu_interesse,
    }
    
    return render(request, 'core/detalhe_problema.html', context)