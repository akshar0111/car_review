from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from my_app.models import complain
from .forms import complainform

def submit_res(request):
    form = complainform()
    if request.method =='POST':
        form = complainform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {'form':form}
    return render(request,'home.html',context)

def panel(request):
    coms = complain.objects.all()    
    return render(request,'panel.html',{'coms':coms})

def del_item(request):
    delete_id  = int(request.GET["num1"])
    try:
        del_obj = complain.objects.get(id = delete_id)
        del_obj.delete()
        return render(request,'del.html',{'item_deleted':True})        
    except:
        return render(request, 'del.html',{'item_deleted':False})