from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django import forms
from django.contrib.auth.password_validation import validate_password

class CustomLoginForm(forms.Form):
    email = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        validate_email(email)
        data = {'email': email}
        try:
            get_user_model().objects.get(**data)
        except get_user_model().DoesNotExist:
            raise ValidationError(
                _('This {} does not exist'.format(list(data.keys())[0])))
        else:
            return email


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Nombre'}))
    description = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Descripción'}))
    email = forms.CharField(max_length=256, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Contraseña'}),validators=[validate_password])

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("This email address is already exists.")
        return email

    class Meta:
        model = get_user_model()
        fields = ("password", "email", "name", "description")
