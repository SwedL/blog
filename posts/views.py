from django.shortcuts import render
from django.http import HttpResponse

people = [
    {'name': 'Жанна Ивановна Бобылева', 'age': 28, 'phone': '+72609577301'},
    {'name': 'Спиридон Феликсович Алексеев', 'age': 48, 'phone': '8 445 133 42 50'},
    {'name': 'Лыткина Зоя Рубеновна', 'age': 34, 'phone': '84061070300'},
    {'name': 'Олимпиада Святославовна Петухова', 'age': 70, 'phone': '8 740 992 96 95'},
    {'name': 'Лазарева Нина Кирилловна', 'age': 67, 'phone': '89040731989'},
    {'name': 'Каллистрат Ильич Ширяев', 'age': 63, 'phone': '+7 418 298 8976'},
    {'name': 'Евсеев Любосмысл Чеславович', 'age': 47, 'phone': '83111461302'},
    {'name': 'Прохор Харламович Артемьев', 'age': 47, 'phone': '+77827445919'},
    {'name': 'Кондрат Игнатьевич Ершов', 'age': 35, 'phone': '+7 419 594 39 00'},
    {'name': 'Ипат Власович Ильин', 'age': 47, 'phone': '88004779773'}
]

def index_info(request):
    return render(request, 'posts/list_detail.html')

def info_kiany(request):
    data = {
        'year_born': '1964',
        'city_born': 'Бейрут',
        'movie_name': 'На гребне волны',
    }
    return render(request, 'posts/info_kiany.html', context=data)

def get_guinness_world_records(request):
    context = {
        'power_man': 'Narve Laeret',
        'bar_name': 'Bob’s BBQ & Grill',
        'count_needle': 1790,
    }
    return render(request, 'posts/guinnessworldrecords.html', context=context)


def get_info_number(request, number):
    data = {
        'number': number,
    }
    return render(request, 'posts/detail_by_number.html', context=data)

def get_info_post(request, name):
    data = {
        'name': name
    }
    return render(request, 'posts/detail_by_name.html', context=data)

def get_info_people(request):
    context = {
        'people': people
    }
    return render(request, 'posts/people.html', context=context)
