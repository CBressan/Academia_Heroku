from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno_Usuario
from .forms import UserRegistrationForm


@login_required
def user_login(request):
    current_user = request.user
    if current_user.is_staff:
        return redirect('user_list')
    else:
        return render(request, 'alunos/ficha.html', {"pessoa": current_user})


@login_required
def user_list(request):
    pessoa = Aluno_Usuario.objects.all()
    return render(request, 'alunos/user.html', {"pessoa": pessoa})


@login_required
def associate(request, id):
    pessoa = get_object_or_404(Aluno_Usuario, pk=id)
    return render(request, 'alunos/ficha.html', {"pessoa": pessoa})


@login_required
def user_update(request, id):
    pessoa = get_object_or_404(Aluno_Usuario, pk=id)
    form = UserRegistrationForm(request.POST or None, request.FILES or None, instance=pessoa)
    if form.is_valid():
        form.save()
        return redirect('alunos/user_list')
    return render(request, 'alunos/user_form.html', {'form': form})


def create_account(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)

        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.save()
            return render(request, 'alunos/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'alunos/register.html', {'user_form': user_form})

