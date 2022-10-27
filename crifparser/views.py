from importlib.resources import files
from multiprocessing import context
from django.shortcuts import render
from django.http import FileResponse, HttpResponse,request, response
from crifparser.forms import clientform
from crifparser.models import crifForm
from crifparser.format_tool import parser
import django
#import joblib
django.setup()
#from django.views.decorators.csrf import csrf_protect 

#@csrf_protect
def home(request):
    context ={}
    form = clientform(request.POST or None, request.FILES or None)
    if request.method=="POST":
        form = clientform(request.POST)
        post=clientform()
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
            #return render(request,'info_review.html')
            
    else:
        form = crifForm()
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

    clientinfo = {"client" : clientinfodata}

    return render(request,'info_review.html',clientinfo)

def download_zip(request):
    #get zip file and return complete html
    clientinfodata = crifForm.objects.get(id=2)
    f_i_code = clientinfodata.f_i_code
    branch_code = clientinfodata.branch_code
    last_acc_date = clientinfodata.last_acc_date
    
    code = clientinfodata.code
    corr_flag = clientinfodata.corr_flag

    subdata = "C:/Users/Juniqua/Desktop/crif/uploads/subject.xlsx"
    condata = "C:/Users/Juniqua/Desktop/crif/uploads/contract.xlsx"

    inp = [f_i_code,branch_code,last_acc_date,code,corr_flag]
    #files = 'C:/Users/Juniqua/Desktop/crif/downloads/CRIFCONTRACTDATA_BPARSING.xlsx'
    parser(inp, subdata,condata)
    #pyparser = joblib.load('parserpy.py')
    #pklparser = joblib.load('C:/Users/Juniqua/Desktop/crif/crifparser/parserpkl.pkl')
    #pyparser = joblib.load('C:/Users/Juniqua/Desktop/crif/crifparser/parserpy.py')
    #pklparser(inp,subdata,condata)
    #pyparser(inp,subdata,condata)
    #pars(inp,subdata,condata)
    #import datetime as dt
    #today = dt.date.today()
    #filedate = today.strftime('%Y%m%d')
    #download_location = 'C:/Users/Juniqua/Desktop/crif/downloads'
    #date_and_code = str(download_location + filedate +'_'+ f_i_code+'.zip')
    return render(request,'download_zip.html',)

def get_zip(response):
    import datetime as dt
    today = dt.date.today()
    filedate = today.strftime('%Y%m%d')
    clientinfodata = crifForm.objects.get(id=2)
    f_i_code = clientinfodata.f_i_code
    
    date_and_code = str('downloads/'+ filedate +'_'+ f_i_code+'.zip')
    file_name = (filedate +'_'+ f_i_code+'.zip') 
    f_data =  open(date_and_code, 'rb')
    f_data = f_data.read()
    # generate the file
    response = HttpResponse(f_data, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="' + file_name+'"'
    return response
    