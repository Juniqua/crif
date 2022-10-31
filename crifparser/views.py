from importlib.resources import files
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import FileResponse, HttpResponse,request, response
from crifparser.forms import clientform,CreateUserForm
from crifparser.models import crifForm
from crifparser.format_tool import parser
import django
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
django.setup()
from django.contrib.auth.decorators import login_required

#@csrf_protect
def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        form = CreateUserForm()
        if request.method=="POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account created for ' + user)
                return redirect('login')
        
        context = {'form':form}
        return render(request,'accounts/register.html',context)   

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
                    
            if user is not None:
                login(request, user)
                return redirect('home')
            
            else:
                messages.info(request, 'Username OR password is incorrect')
                #return render(request, 'accounts/login.html', context)
            
        context = {}
        return render(request, 'accounts/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    context ={}
    
    form = clientform()
    if request.method=="POST":
        form = clientform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('info_review')
        else:
            form=clientform()
    return render(request, 'index.html') 
"""        post=clientform()
        post.f_i_code= request.POST.get('f_i_code')
        post.branch_code= request.POST.get('branch_code')
        post.last_acc_date= request.POST.get('last_acc_date')
        post.date_of_prod= request.POST.get('date_of_prod')
        post.code= request.POST.get('code')
        post.corr_flag= request.POST.get('corr_flag')
        post.contract_columns= request.FILES.get('contract_columns')
        post.subject_columns= request.FILES.get('subject_columns')
        post.save(force_insert=True)
        # check if form data is valid
        
            return HttpResponse(request,"Saved")"""
            
       
    # "Hello, Django!")
inp = ['f_i_code','branch_code','last_acc_date','date_of_prod','code','corr_flag']
ffields = ['contract_columns','subject_columns']

@login_required(login_url='login')
def info_review(request):
    clientinfodata = crifForm.objects.get(id=1)
    f_i_code = clientinfodata.f_i_code
    branch_code = clientinfodata.branch_code
    last_acc_date = clientinfodata.last_acc_date
    date_of_prod = clientinfodata.date_of_prod
    code = clientinfodata.code
    corr_flag = clientinfodata.corr_flag

    clientinfo = {"client" : clientinfodata}

    return render(request,'info_review.html', clientinfo)

@login_required(login_url='login')
def download_zip(request):
    #get zip file and return complete html
    clientinfodata = crifForm.objects.get(id=1)
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

@login_required(login_url='login')
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
    