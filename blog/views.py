from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

def info_blog(request):
    response = render_to_string('blog/index.html')
    return HttpResponse(response)


