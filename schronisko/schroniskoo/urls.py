from django.urls import path
from . import views

urlpatterns = [
    path('schroniskoo/', views.pies_list.as_view()),
    path('schroniskoo/<int:pk>/', views.pies_detail.as_view()),
    path('schroniskoo/', views.box_list.as_view()),
    path('schroniskoo/', views.adopter_list.as_view()),
    path('schroniskoo/<int:pk>/', views.adopter_detail.as_view()),
    path('schroniskoo/', views.adopcja_list.as_view()),
    path('schroniskoo/<int:pk>/', views.adopcja_detail.as_view()),
    path('schroniskoo/', views.UserList.as_view()),
    path('schroniskoo/<int:pk>/', views.UserDetail.as_view()),
]
