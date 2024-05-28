from django.shortcuts import render,redirect


# Create your views here.
from .forms import UserCreationForm
from django.views import View
from django.contrib.auth import authenticate,login
class Register(View):
	template_name = "registration/register.html"
	def get(self,request):
		context={
			'form':UserCreationForm()
		}
		return render(request,self.template_name,context=context)
	def post(self,request):
		form =UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username,password=password)
			login(request,user)
			return redirect('main')
		context={
			'form':form
		}
		return render(request,self.template_name,context)