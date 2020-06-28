from django.urls import path
from . import views

urlpatterns = [
    path('',views.submit_res),
    path('panel/',views.panel),
    path('panel/del_item/',views.del_item),
]