from django.urls import path
from django.contrib.auth import views as auth_views
from home import views
from home.views import ContactView, success, LocationView

urlpatterns = [
    path('', views.index, name='index'),
    path('bookpackage/', views.bookpackage, name='bookpackage'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('about/', views.about, name='about'),
    path('password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='pages/password_change_done.html'
    ), name="password_change_done"),
    path('password-reset/', views.UserPasswordResetView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='pages/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='pages/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('contact-us/', ContactView.as_view(), name='contact_us'),
    path('success/', success, name='success'),
    path('location/', LocationView.as_view(), name='location'),

]
