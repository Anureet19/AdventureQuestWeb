from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime


from .forms import BookingForm
from .models import Tier, Reservation, Package, Contact, Directions
from theme_material_kit.forms import LoginForm, RegistrationForm, UserPasswordResetForm, UserSetPasswordForm, \
    UserPasswordChangeForm
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import ContactForm
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.conf import settings


# Create your views here.
@login_required(login_url='/login/')
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


@login_required(login_url='/login/')
def bookpackage(request):
    package_id = request.GET['package_id']
    package = Package.objects.all().get(id=package_id)
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
            return redirect('/login')
        else:
            print("Registration failed!")
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'pages/sign-up.html', context)


def about(request):
    return render(request, 'pages/about.html')


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'pages/password_reset.html'
    form_class = UserPasswordResetForm


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'pages/password_reset_confirm.html'
    form_class = UserSetPasswordForm


class UserPasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'pages/password_change.html'
    form_class = UserPasswordChangeForm


class ContactView(FormView):
    template_name = 'pages/contact_us.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            form.save()

            # get the form data
            full_name = form.cleaned_data.get('full_name')
            email = form.cleaned_data.get('email')
            message = form.cleaned_data.get('message')

            # send email
            subject = 'New contact form submission'
            body = f'Full Name: {full_name}\nEmail: {email}\nMessage: {message}'
            sender_email = email
            recipient_list = ['adventure.quest.web@gmail.com']
            print("sending")
            send_mail(subject, body, sender_email, recipient_list)
            print("sent")

            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def success(request):
    return render(request, 'pages/success.html')

class LocationView(TemplateView):
    template_name = 'pages/location.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY
        return context

api_key = settings.GOOGLE_MAPS_API_KEY
url = f"https://maps.googleapis.com/maps/api/js?key={api_key}"


# Create your views here.
def bookingview(request):
    if request.method == 'POST':
        print(request.POST)
        full_name = request.POST.get('full_name', False)
        total_person = int(request.POST.get('number_of_people', False))
        entry = request.POST.get('entry', False)
        package_id = request.POST.get('package_id', False)
        current_user = request.user
        user_object = User.objects.all().get(username=current_user)
        package_object = Package.objects.all().get(id=package_id)
        price_per_ticket = package_object.price
        total_price = total_person * price_per_ticket
        booking_id = str(package_id) + str(datetime.datetime.now())
        reservation = Reservation()

        reservation.full_name = full_name
        reservation.number_of_people = total_person
        reservation.entry_date = entry
        reservation.package = package_object
        reservation.user = user_object
        reservation.price_paid = total_price
        reservation.booking_id = booking_id

        reservation.save()
        return HttpResponse(render(request, 'pages/bookingconfirm.html', {'price': total_price, 'booking_id': booking_id}))
    else:
        return HttpResponse('Access Denied')

class LocationView(TemplateView):
    template_name = 'pages/location.html'

    def get_context_data(self, **kwargs):
        directions = Directions.objects.all()

        context = super().get_context_data(**kwargs)
        context['GOOGLE_MAPS_API_KEY'] = settings.GOOGLE_MAPS_API_KEY
        context['directions'] = directions
        return context

api_key = settings.GOOGLE_MAPS_API_KEY
url = f"https://maps.googleapis.com/maps/api/js?key={api_key}"


