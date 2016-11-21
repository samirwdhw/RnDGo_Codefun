from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from forms import UserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import redirect
# Create your views here.
# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="login/")

def home(request):
	return render(request,"home.html")

def addUser(request):

	if request.method == "POST":
		form = UserForm(request.POST)

		if form.is_valid():
			post = form.save(commit=False)
			new_user = User.objects.create_user(**form.cleaned_data)
			new_user.save()
			return redirect('/login/')
	else:
		form = UserForm()

	return render(request, 'signUp.html', {'form':form})