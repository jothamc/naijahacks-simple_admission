from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password

from .models import User
# ,Suggest
# from clients.models import Client
# from riders.models import Rider

# Create your views here.
#Have views/models that handle Clients and Riders different or use the User model with the 'is_rider' field?
class HandyUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = UserCreationForm.Meta.fields + ('email',)

def RegisterView(request):
	if request.method == "GET":
		form = HandyUserCreationForm()
	elif request.method == "POST":
		form = HandyUserCreationForm(request.POST)
		user = User(username = request.POST['username'])
		validate_password(request.POST['password1'],user=user)


		if form.is_valid():
			form.save()
			user = User.objects.get(username=request.POST['username'])
			username = request.POST['username']
			password = request.POST['password1']
			auth_user = authenticate(request,username=username,password=password)
			if auth_user is not None:
				login(request,auth_user)
			return redirect("/user/")
	return render(request,"registration/register.html",{"form":form})


# class SuggestDetailView(DetailView):
# 		model = Suggest
# 		template_name = "suggest.html"
# )


from django import forms
from crawler import courses

all_courses = []
count = 0

for i in courses:
	all_courses.append( tuple([count,i]) )
	count = count + 1

class suggestForm(forms.Form):
	"""suggestForm definition."""

	SSCE = (
		("A1","A1"),
		("B2","B2"),
		("B3","B3"),
		("C4","C4"),
		("C5","C5"),
		("C6","C6"),
		("D7","D7"),
		("E8","E8"),
		("F9","F9"),
	)
	course = forms.ChoiceField(choices=(all_courses))
	subject_1 = forms.IntegerField(max_value=100,min_value=0,label="Use of English")
	subject_2 = forms.IntegerField(max_value=100,min_value=0,)
	subject_3 = forms.IntegerField(max_value=100,min_value=0,)
	subject_4 = forms.IntegerField(max_value=100,min_value=0,)

	ssce_1 = forms.ChoiceField(choices=SSCE,label = "English Language")
	ssce_2 = forms.ChoiceField(choices=SSCE,label = "Subject 2")
	ssce_3 = forms.ChoiceField(choices=SSCE,label = "Subject 3")
	ssce_4 = forms.ChoiceField(choices=SSCE,label = "Subject 4")
	ssce_5 = forms.ChoiceField(choices=SSCE,label = "Subject 5")
	ssce_6 = forms.ChoiceField(choices=SSCE,label = "Subject 6")
	ssce_7 = forms.ChoiceField(choices=SSCE,label = "Subject 7")
	ssce_8 = forms.ChoiceField(choices=SSCE,label = "Subject 8")


	

def Suggest(request):
	if request.method == "GET":
		form = suggestForm()
	return render(request,"suggest.html",{"form":form})