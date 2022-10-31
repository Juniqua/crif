from django.db import models
from django.forms import CharField, FileField, IntegerField, DateField


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
    
    class Meta:
        db_table = "client"

    def __str__(self):
        return self.f_i_code
        
        
                
