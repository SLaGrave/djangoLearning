from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('ranks/', views.rank_list, name='rank_list'),
    path('ranks/<str:alias>', views.player_detail, name='player_detail'),
    path('report/', views.report, name='report'),
]
