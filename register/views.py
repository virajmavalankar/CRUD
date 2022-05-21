from django.shortcuts import render
from register.models import UserModel
from django.contrib import messages
from register.forms import Empforms


def showemp(request):
	showall = UserModel.objects.all()
	return render(request, 'index.html', {"data":showall})

def insertemp(request):
	if request.method=="POST":
		if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('phonenumber'):
			saverecord = UserModel()
			saverecord.firstname=request.POST.get('firstname')
			saverecord.lastname=request.POST.get('lastname')
			saverecord.email=request.POST.get('email')
			saverecord.phonenumber=request.POST.get('phonenumber')
			saverecord.save()
			messages.success(request, 'Employee '+saverecord.firstname+' is saved successfully')
			return render(request, 'insert.html')
	else:

		return render(request, 'insert.html')

def editemp(request, id):
	editempobj = UserModel.objects.get(id=id)
	return render(request, 'edit.html', {'UserModel':editempobj})

def updateemp(request, id):
	updateemp = UserModel.objects.get(id=id)
	form = Empforms(request.POST,instance=updateemp)
	if form.is_valid():
		form.save()
		messages.success(request, 'Record Updated successfully')
		return render(request,'edit.html', {"UserModel":updateemp})


def delemp(request,id):
	delemployee=UserModel.objects.get(id=id)
	delemployee.delete()
	showdata=UserModel.objects.all()
	return render(request, "index.html", {"data":showdata})