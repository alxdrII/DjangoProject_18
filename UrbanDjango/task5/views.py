from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserRegister

users = {
    'petrov': '12345678',
    'ivanov': '87654321',
    'sidorov': '00000000',
    'user': '12121212',
}


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'

            elif int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'

            elif username in users.keys():
                info['error'] = 'Пользователь уже существует'

            else:
                users[username] = password
                return HttpResponse(f'<h2 align="center">Приветствуем, {username}!</h2>')

    else:
        form = UserRegister()

    return render(request, 'fifth_task/registration_page1.html', {'form': form, 'info': info})


def sign_up_by_html(request):
    info = {}

    if request.method == 'POST':
        # Получаем данные
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'

        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'

        elif username in users.keys():
            info['error'] = 'Пользователь уже существует'

        else:
            users[username] = password
            return HttpResponse(f'<h2 align="center">Приветствуем, {username}!</h2>')

    return render(request, 'fifth_task/registration_page.html', {'info': info})