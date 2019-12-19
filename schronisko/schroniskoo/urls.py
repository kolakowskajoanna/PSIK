from django.urls import path
from . import views

urlpatterns = [
    path('schroniskoo/', views.pies_list),
    path('schroniskoo/<int:pk>/', views.pies_detail),
    path('schroniskoo/', views.box_list),
    path('schroniskoo/', views.adopter_list),
    path('schroniskoo/<int:pk>/', views.adopter_detail),
    path('schroniskoo/', views.adopcja_list),
    path('schroniskoo/<int:pk>/', views.adopcja_detail),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]
