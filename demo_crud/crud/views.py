from django.shortcuts import render,redirect
from .models import Customer

def index(request):
    data={}
    if request.method =="POST":
        a = request.POST["customer_name"]
        b = request.POST["customer_email"]
        c = request.POST["customer_city"]
        obj = Customer(cname =a,cemail=b, ccity=c)
        obj.save()
    data["record"] = Customer.objects.all()
    return render(request,"index.html",data)    


def customer_edit(request,id):
    data = {}
    if request.method =="POST":
        a = request.POST["customer_name"]
        b = request.POST["customer_email"]
        c = request.POST["customer_city"]
        obj=Customer.objects.get(cid=id)
        obj.cname= a
        obj.cemail = b
        obj.ccity = c
        obj.save()
    data["record"]=Customer.objects.get(cid=id)
    return render(request,"customer_edit.html",data)    

def customer_delete(request,id):
    Customer.objects.get(cid=id).delete()
    return redirect(index)