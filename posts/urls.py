from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_info),
    path('kiany', views.info_kiany),
    path('records', views.get_guinness_world_records),
    path('<int:number>', views.get_info_number),
    path('<str:name>', views.get_info_post)
]
