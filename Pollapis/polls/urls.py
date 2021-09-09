from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.polls_list, name='polls'),
    path('<int:pk>', views.polls_detail, name='detail'),
]