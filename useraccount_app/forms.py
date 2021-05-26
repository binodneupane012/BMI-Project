from django import forms
from useraccount_app.models import Profile
from django.contrib.auth.forms import UserCreationForm
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

