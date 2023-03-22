from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bookpackage/', views.bookpackage, name='bookpackage'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.user_logout_view, name='logout'),
    path('register/', views.registration, name='register'),
    path('about/', views.about, name='about'),

]
