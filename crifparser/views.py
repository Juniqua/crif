from multiprocessing import context
from django.shortcuts import render
from django.http import FileResponse, HttpResponse,request, response
from crifparser.forms import clientform
from crifparser.models import crifForm, crifFormInfo
from crifparser.format_tool import parser
import django
import joblib
django.setup()
#from django.views.decorators.csrf import csrf_protect 

#@csrf_protect
def home(request):
    context ={}
    form = clientform(request.POST or None, request.FILES or None)
    if request.method=="POST":
        form = clientform(request.POST)
        post=crifForm()
        post.f_i_code= request.POST.get('f_i_code')
        post.branch_code= request.POST.get('branch_code')
        post.last_acc_date= request.POST.get('last_acc_date')
        post.date_of_prod= request.POST.get('date_of_prod')
        post.code= request.POST.get('code')
        post.corr_flag= request.POST.get('corr_flag')
        post.contract_columns= request.FILES.get('contract_columns')
        post.subject_columns= request.FILES.get('subject_columns')
        post.save()
        # check if form data is valid
        if form.is_valid():
            form.save()
            #return render(request,'format_complete.html', {'content': items} )
            
    else:
        form = clientform()
        # save the form data to model
    context['form']= form
    # render function takes argument  - request
    # and return HTML as response
    return render(request, 'index.html',{'form':form}) # "Hello, Django!")
inp = ['f_i_code','branch_code','last_acc_date','date_of_prod','code','corr_flag']
ffields = ['contract_columns','subject_columns']

def info_review(request):
    clientinfodata = crifForm.objects.get(id=1)
    f_i_code = clientinfodata.f_i_code
    branch_code = clientinfodata.branch_code
    last_acc_date = clientinfodata.last_acc_date
    date_of_prod = clientinfodata.date_of_prod
    code = clientinfodata.code
    corr_flag = clientinfodata.corr_flag

    subdata = clientinfodata.subject_columns
    condata = clientinfodata.contract_columns


    inp = [f_i_code,branch_code,last_acc_date,date_of_prod,code,corr_flag]

    clientinfo = {"client" : clientinfodata}
    #parser(inp, subdata,condata)
    #pyparser = joblib.load('parserpy.py')
    #pklparser = joblib.load('C:/Users/Juniqua/Desktop/crif/crifparser/parserpkl.pkl')
    pyparser = joblib.load('C:/Users/Juniqua/Desktop/crif/crifparser/parserpy.py')
    #pklparser(inp,subdata,condata)
    pyparser(inp,subdata,condata)
    #pars(inp,subdata,condata)

    return render(request,'info_review.html',clientinfo)

def get_zip():
    #get zip file and return complete html
    return
