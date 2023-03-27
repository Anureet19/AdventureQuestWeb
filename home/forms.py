from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UsernameField, \
    PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from django.forms import ModelForm
from .models import Reservation, GroupBook, Contact


class BookingForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['full_name', 'entry_date', 'package', 'number_of_people']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control',})


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"class": "form-control"}))

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password", "class": "form-control"}),
    )


class UserPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )


class UserSetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New Password"
    )
    new_password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm New Password"
    )


class UserPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Old Password'
    )

    new_password1 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="New Password"
    )

    new_password2 = forms.CharField(
        max_length=50,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label="Confirm New Password"
    )

class GroupPassForm(forms.ModelForm):
    class Meta:
        model = GroupBook
        fields = ['members', 'pass_type', 'sub_pass_type', 'number_of_pass', 'total_cost', 'date']
        widgets = {
            'pass_type': forms.RadioSelect(attrs={'class': 'my-field-radio'}),
            'sub_pass_type': forms.Select(attrs={'class': 'my-field-class'}),
            'members': forms.TextInput(attrs={'class': 'my-field-class'}),
            'number_of_pass': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'my-field-class'}),
            'total_cost': forms.TextInput(attrs={'readonly': 'readonly', 'class': 'my-field-class'}),
        }

    class Media:
        css = {
            'all': ('home/static/deals.css',)
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'How can we help you?'}),
        }
