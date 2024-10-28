from django.shortcuts import render


def game_products(request):
    context = {'games': ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']}
    return render(request, 'fourth_task/games.html', context)
