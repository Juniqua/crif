from multiprocessing import context
from django.shortcuts import render
from django.http import FileResponse, HttpResponse,request, response
from crifparser.forms import clientform
from crifparser.models import crifForm
import django
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
def format_complete(request):
    inp_dict ={}
    form = clientform(request.GET or None, request.FILES or None)
    def inputinfo(inp):
        i = 0
        while i < len(inp):
            inp_dict = {inp[i]:request.GET[inp[i]]}
            i+=1
    if request.method=="GET":
        inputinfo(inp)

        
        #post.contract_columns= request.FILES.get('contract_columns')
        #post.subject_columns= request.FILES.get('subject_columns')
        items = inp
        #resp = FileResponse(open("C:/Users/Juniqua/Desktop/crif/uploads/contract.xlsx", 'rb'),as_attachment=True)#filename=
    return render(request,'format_complete.html',{'content':items})

def get_zip():
    #get zip file and return complete html
    return
