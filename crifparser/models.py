#from tkinter import CASCADE
from django.db import models
#from wsgiref.validate import validator
from django.forms import CharField, FileField, IntegerField, DateField
#from pygments.lexers import get_all_lexers
#from pygments.styles import get_all_styles

#LEXERS = [item for item in get_all_lexers() if item[1]]
#ANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

# Create your models here.
class crifForm(models.Model):
  f_i_code = models.CharField("Financial Institution Code - XXXXX",max_length=5)
  branch_code = models.CharField("Branch Code - BRANCH00",max_length=8)
  last_acc_date = models.CharField("Last Accounting Date - DDMMYYYY - 00000000", max_length=8)
  date_of_prod = models.CharField("Production Date - 00000000", max_length=8)
  code = models.IntegerField("Code - 000")
  corr_flag = models.CharField("Correction flag - '1' or ' '",max_length=1)
  contract_columns = models.FileField("Submit 'CONTRACT.xlsx' File Here",upload_to='uploads/')
  subject_columns = models.FileField("Submit 'SUBJECT.xlsx' File Here",upload_to='uploads/')
  #submit = models. SubmitField("Format")
  class Meta:
      db_table = "client"
  def __str__(self):

      return self.f_i_code

class crifFormInfo(models.Model):
    crifform = models.ForeignKey(crifForm, on_delete=models.CASCADE)
    f_i_code = models.CharField("Financial Institution Code - XXXXX",max_length=5)
    branch_code = models.CharField("Branch Code - BRANCH00",max_length=8)
    last_acc_date = models.CharField("Last Accounting Date - DDMMYYYY - 00000000", max_length=8)
    date_of_prod = models.CharField("Production Date - 00000000", max_length=8)#,auto_now_add = True
    code = models.IntegerField("Code - 000")
    corr_flag = models.CharField("Correction flag - '1' or ' '",max_length=1)
    class Meta:
        db_table = "Client_Info"
    def __str__(self):
        return self.f_i_code
        
        
        
