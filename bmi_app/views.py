from django.shortcuts import render, reverse, Http404, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from bmi_app.forms import BmimeasuremantForm
from bmi_app.models import BMIMeasurement, Suggestion
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from  django.template.loader import render_to_string



# Create your views here.

def bmi_list(request):
    bmimeasurements = BMIMeasurement.objects.filter(user=request.user)
    context = {"bmimeasurements":bmimeasurements}
    return render(request, 'bmi_list.html', context)


@login_required
def bmi_calculate(request):
    is_form_submitted = False
    bmi = None
    suggestion = None
    message  = None
    form = BmimeasuremantForm(request.POST or None)
    if form.is_valid():
        bmimeasurement=form.save(commit=False)
        bmimeasurement.user = request.user
        bmimeasurement.save()
        is_form_submitted = True
        bmi=bmimeasurement.bmi()
        if bmi <= 18.5:
            suggestion = "Underweight"
        elif bmi >= 18.6 and bmi <=24.9 :
            suggestion = "Normal weight"
        elif bmi > 25 and bmi < 29.9:
            suggestion = "Overweight"
        else:
            suggestion = "obsessed"
        message = suggestion

    context = {"form": form, "bmi": bmi, "is_form_submitted": is_form_submitted, "suggestion": suggestion, "message":message}
    return render(request, 'form.html', context)

def bmi_edit(request, id):
    bmimeasurement = get_object_or_404(BMIMeasurement, id=id)
    form = BmimeasuremantForm(request.POST or None, instance=bmimeasurement)
    if form.is_valid():
        form.save
        return HttpResponseRedirect(reverse("bmi_app:bmi_list"))
    context = {"form": form}
    return render(request, 'form.html', context)

def bmi_delete(request, id):
    bmimeasurement = get_object_or_404(BMIMeasurement, id=id)
    bmimeasurement.delete()
    return HttpResponseRedirect(reverse("bmi_app:bmi_list"))


def send_report(request):
    bmi = round(BMIMeasurement.bmi(BMIMeasurement.objects.all().last()),2)
    if bmi <= 18.5:
        message = "Underweight. You need to increase your weight"
    elif bmi >= 18.6 and bmi <=24.9:
        message = "Normal weight. You are fit and fine keep it up"
    elif bmi > 25 and bmi < 29.9:
        message = "Overweight. You need to reduce your weight"
    else:
        message = "obsessed. You are very overweight, please consult a doctor"
    send_mail(  "BMI report",
                message + " Your BMI is "+ str(bmi),
                "ytddash@gmail.com",
                ["binod997243@gmail.com"],
                # [request.user.profile.email],
                # false_silently = False
            )
    return render(request, "report.html",{})


