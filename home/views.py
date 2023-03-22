from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    # Page from the theme 
    return render(request, 'pages/index.html')
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


def about(request):
    return render(request, 'pages/about.html')

