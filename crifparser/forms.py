from django import forms
from crifparser.models import crifForm

class clientform(forms.ModelForm):
    class Meta:
        model = crifForm
        fields = "__all__" #['f_i_code','branch_code','last_acc_date','date_of_prod','code','corr_flag']