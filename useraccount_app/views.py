from django.shortcuts import render, reverse, Http404, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from useraccount_app.forms import ProfileForm
from django.contrib.auth.views import LoginView
from django.contrib import messages
from useraccount_app.models import Profile
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from useraccount_app.forms import CustomSignupForm
from django.contrib.auth import authenticate, login
from  django.template.loader import render_to_string
from django.core.mail import send_mail

# Create your views here.


def profile_list(request):
    profiles = Profile.objects.filter(user=request.user)
    context = {"profiles": profiles}
    print (context)
    return render(request, 'profile_list.html', context)

# def profile_add(request):
#     form = ProfileForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect(reverse("useraccount_app:profile_list"))
#     context = {"form": form}
#     return render(request, 'form.html', context)

def profile_edit(request, id):
    profile = get_object_or_404(Profile, id=id)
    form = ProfileForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("useraccount_app:profile_list"))
    context = {"form": form}
    return render(request, 'profile_form.html', context)


# def profile_delete(request, id):
#     profile = get_object_or_404(Profile, id=id)
#     profile.delete()
#     return HttpResponseRedirect(reverse("useraccount_app:profile_list"))


class UserLogin(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = False


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["next"] = self.request.GET.get("next")
        return context

def signup_view(request):
    form = CustomSignupForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("useraccount_app:login"))
    context = {"form":form}
    return render(request, "register.html", context)

def send_confirm_email(request):
    subject = "Test Subject"
    message = "Test Meassage"
    from_email = "ytddash@gmail.com"
    recipient_list = ["binod997243@gmail.com"]
    context = {"name": "Binod"}
    html_message = render_to_string("user_profile.html")
    res = send_mail(subject, message, from_email,
    recipient_list, html_message=html_message)
    return HttpResponse(res)

