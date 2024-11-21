from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

# Create your views here.
users = ['Den', 'Max', 'Jon', 'Ivan', 'Nik']


def sign_up_by_django(request):
    info = {'error': []}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
        if username not in users and password == repeat_password and int(age) >= 18:
            users.append(username)
            return HttpResponse(f'Приветствуем, {username}')
        elif username in users:
            info['error'] = HttpResponse('Пользователь уже существует')
            return HttpResponse('Пользователь уже существует')
        elif password != repeat_password:
            info['error'] = HttpResponse('Пароли не совпадают')
            return HttpResponse('Пароли не совпадают')
        elif int(age) < 18:
            info['error'] = HttpResponse('Вы должны быть старше 18')
            return HttpResponse('Вы должны быть старше 18')
    else:
        form = UserRegister()
        context = {'info': info, 'form': form}
        return render(request, 'registration_page.html', context)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if username not in users and password == repeat_password and int(age) >= 18:
            users.append(username)
            return HttpResponse(f'Приветствуем, {username}')
        else:
            if username in users:
                info['error'] = 'Пользователь уже существует'
                return HttpResponse('Пользователь уже существует')
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return HttpResponse('Пароли не совпадают')
            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return HttpResponse('Вы должны быть старше 18')
    return render(request, 'registration_page.html', {'info': info})

