from django import forms
from django.forms import widgets
from bmi_app.models import BMIMeasurement

class BmimeasuremantForm(forms.ModelForm):

    class Meta:
        model = BMIMeasurement
        # fields = [ "weight", "height",]
        fields = "__all__"
        exclude = ("user", )

    # def __init__(self, *args, **kwargs):
    #     super(BmimeasuremantForm,self).__init__(*args, **kwargs)
    #     self.fields['user'].empty_label = "Select"
    #     self.fields['user'].required = False

    # widgets = {
    #     'weight':forms.FloatField(attrs={'class':'form-control'}),
    #     'height':forms.FloatField(attrs={'class':'form-control'}),
    # }