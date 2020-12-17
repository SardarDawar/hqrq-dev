from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django.forms import TextInput 
from django.core.exceptions import ValidationError

# user registration form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['email', 'password1', 'password2']

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        qs = get_user_model().objects.filter(email=email)
        if qs.count() > 0:
            raise forms.ValidationError("An account with this email already exists.")
        return email

# user update form
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'image']


class MyPasswordResetForm(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data['email']
        if not get_user_model().objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("Account with this EMAIL does not exist")
        return email
