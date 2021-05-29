from django import forms
from useraccount_app.models import Profile
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CustomSignupForm(UserCreationForm):
    email = forms.EmailField()
    # password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # password2 = forms.CharField(label="Password Again", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    # widgets = {'username':forms.TextInput(attrs={'class':'form-control'})}
    # email = forms.CharField(required=True, widget=forms.EmailField(attrs={'class':'form-control'}))

class MyChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus': True, 'class':'form-control'}),
    )

    new_password1 = forms.CharField(
        label="New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}),
    )

    new_password2 = forms.CharField(
        label="New Password Again",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'class':'form-control'}),
    )