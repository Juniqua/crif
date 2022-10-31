from dataclasses import field
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crifparser.models import crifForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']

class clientform(forms.ModelForm):
    class Meta:
        model = crifForm
        fields = "__all__" #['f_i_code','branch_code','last_acc_date','date_of_prod','code','corr_flag']

class fileform(forms.ModelForm):
    class Meta:
        model = crifForm
        fields = ["subject_columns","contract_columns"]
        #exclude = ['f_i_code','branch_code','last_acc_date','date_of_prod','code','corr_flag']

class infoform(forms.ModelForm):
    class Meta:
        model = crifForm
        fields = ['f_i_code','branch_code','last_acc_date','date_of_prod','code','corr_flag']
        #exclude = ["subject_columns","contract_columns]

