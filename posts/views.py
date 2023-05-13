from django.shortcuts import render
from django.http import HttpResponse


def index_info(request):
    return render(request, 'posts/list_detail.html')

def get_info_number(request, number):
    return HttpResponse(f'Здесь содержится информация о посте под номером {number}')

def get_info_post(request, post):
    return HttpResponse(f'Информация о посте {post}')
