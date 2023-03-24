from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pages/login/', views.UserLoginView.as_view(), name='login'),
    path('pages/logout/', views.user_logout_view, name='logout'),
    path('pages/register/', views.registration, name='register'),
]
