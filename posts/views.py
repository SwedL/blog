from django.shortcuts import render
from django.http import HttpResponse


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
