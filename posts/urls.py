from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_info),
    path('<int:number>', views.get_info_number),
    path('<str:post>', views.get_info_post)
]
