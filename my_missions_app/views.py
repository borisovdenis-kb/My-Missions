from random import choice
from django.contrib import auth
from django.shortcuts import render
from django.shortcuts import render_to_response
from  django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from my_missions import config
from my_missions_app.models import *

# Create your views here.


def login_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/")

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse('User is not active.')
        else:
            return HttpResponse('Invalid Login or Password')
    else:
        return render_to_response('login.html')


def root_view(request):
    """
        Функция открытия соответствующая url: my_mission.ru
        Юзер заходит по этой ссылке.
        Далее
        Если у него уже созданны категории и заметки, то
            Смотрим какие последий раз юзер просматривал задачу и
            перебрасываем юзера на соответствующий url: ...\id_user\cat_id
        Иначе
            Отображаем страницу с предлажением создать категорию и задачу
            После создания категории перебрасываем его
            на соответствующий url: .../id_user/cat_id
    """
    if request.user.is_authenticated():
        user = CustomUser.objects.get(username=request.user.username)
        context = {'username': user.username}
        if user.last_cat:
            return HttpResponseRedirect(user.last_cat)
        else:
            # пока еще не создано ни одной категории
            context['cat_empty'] = True
            return render_to_response('home.html', context)
    else:
        return HttpResponseRedirect("/login")


def tasks_view(request, user_id, cat_id):
    """
        Функция вывода задач из соответствующей категории
        Категория определяется из ссылки
        url: /id_user/cat_id
        Причем будет отображаться последняя открытая категория
    """
    print('tasks_view')
    if request.user.is_authenticated():
        user = CustomUser.objects.get(username=request.user.username)
        cats = Category.objects.filter(user_id_id=user_id)
        missions = Missions.objects.filter(cat_id_id=cat_id)
        context = {'username': user.username}

        # помечаем последнюю открытую категорию
        cat_list = []
        for cat in cats:
            if cat.cat_id == int(cat_id):
                cat_list.append((cat, True))
            else:
                cat_list.append((cat, False))

        print(cat_list)

        # задаем случайный набор цветов для каждой задачи
        missions_list = []
        for mission in missions:
            color_set = choice(list(config.colors.values()))
            missions_list.append((mission, color_set))

        context['cats'] = cat_list
        context['missions'] = missions_list

        return render_to_response('home.html', context)
    else:
        return HttpResponseRedirect("/login")