from django.shortcuts import render


def info_blog(request):
    return render(request, 'blog/index.html')


def b_table(request):
    return render(request, 'blog/b_table.html')
