from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from djhango.db.models import Sum
from .models import Gasto
from .forms import GastoForm

def home(request):
    gastos = Gasto.object.filter(usuario=request.user).order_by('-data')
    total = gastos.aggregate(Sum('valor'))['valor__sum'] or 0
    return render(request, 'gastos/home.html', {'gastos': gastos, 'total': total})


def novo_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            gasto = form.save(commit=False)
            gasto.usuario = request.user
            gasto.save()
            return redirect('home')
    else:
        form = GastoForm()
    return render(request, 'gastos/form_gasto.html', {'form': form})

def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        from = UserCreationForm()
return render(request, 'gastos/cadastro.html', {'form'; form})
