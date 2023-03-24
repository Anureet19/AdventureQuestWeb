from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tier, Reservation, Package
from theme_material_kit.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, \
    UserPasswordChangeForm
from django.contrib.auth import logout

from django.contrib.auth import views as auth_views


# Create your views here.

def index(request):
    all_tier = Tier.objects.values_list('name', 'id').distinct().order_by()
    if request.method == 'POST':
        packages = Package.objects.all().filter(tier__id=int(request.POST['tier_id']))
        print(packages)
        data = {'packages': packages, 'all_tier': all_tier, 'flag': True}
        response = render(request, 'pages/index.html', data)
    else:
        response = render(request, 'pages/index.html', {'all_tier': all_tier})

    return HttpResponse(response)


@login_required
def bookpackage(request):
    package_id = request.GET['package_id']
    package = Package.objects.all().filter(id=package_id)
    return HttpResponse(render(request, 'pages/bookpackage.html', {'package': package}))


class UserLoginView(auth_views.LoginView):
    template_name = 'pages/sign-in.html'
    form_class = LoginForm
    success_url = '/'


def user_logout_view(request):
    logout(request)
    return redirect('/login/')


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            print('Account created successfully!')
            return redirect('/login/')
        else:
            print("Registration failed!")
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'pages/sign-up.html', context)
