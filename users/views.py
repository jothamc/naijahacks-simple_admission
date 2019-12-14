from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password

from .models import User


# Create your views here.
#Have views/models that handle Clients and Riders different or use the User model with the 'is_rider' field?
class UserCreationForm(UserCreationForm):
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


from django import forms
import json

courses_json = open("courses.json")
courses = json.loads( courses_json.read() )
courses_json.close()
all_courses = []
count = 0

for i in courses:
	all_courses.append( tuple([count,i]) )
	count = count + 1
all_courses.sort()

ssce_dict = {
	"A1":1, "B2":2,	"B3":3,
	"C4":4,	"C5":5,	"C6":6,
	"D7":7,	"E8":8,	"F9":9,
}

class suggestForm(forms.Form):
	"""suggestForm definition."""

	def ssce_tuple(ssce_dict):
		all_ssce = []
		for i,j in ssce_dict.items():
			all_ssce.append(tuple([j,i]))
		return tuple(all_ssce)

	SSCE = ssce_tuple(ssce_dict)

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
		return render(request,"profile.html",{"form":form})
	elif request.method == "POST":
		form = suggestForm(request.POST)
		return Results(request)
		# return render(request,"results.html",{"form":form})

import json
universities_courses = json.loads( open("fed_universities_and_courses.json").read() )

def Results(request):
	post = request.POST
	course = all_courses[int(post["course"])]
	chosen_course = course[1]
	english = int(post['subject_1'])
	subject_2 = int( post['subject_2'])
	subject_3 = int( post['subject_3'])
	subject_4 = int( post['subject_4'])
	total_jamb_score = english + subject_2 + subject_3 + subject_4
	results = {
		"Chosen course": chosen_course,
		"Use of English": english,
		"JAMB Subject 2": subject_2,
		"JAMB Subject 3": subject_3,
		"JAMB Subject 4": subject_4,
		"Total JAMB Score": total_jamb_score,
		"SSCE 1":post["ssce_1"],
		"SSCE2":post["ssce_2"],
		"SSCE 3":post["ssce_3"],
		"SSCE 4":post["ssce_4"],
		"SSCCE 5":post["ssce_5"],
		"SSCE 6":post["ssce_6"],
		"SSCE 7":post["ssce_7"],
		"SSCE 8":post["ssce_8"],
		"universities": course_check(chosen_course),
		}
	return render(request,"results.html",{"results":results})


def course_check(course):
	universities = []
	for i in universities_courses:
		if course in universities_courses[i]:
			universities.append(i)
	return universities

def jamb_score_check(jamb_score,school,course):
	if jamb_score >= school.course.cut_off_score:
		return True
	return False

def ssce_score_check(ssce_scores,school,course):
	scores = {}
	for subject in ssce_scores:
		if subject in school.course.ssce_subjects and subject.score > school.course.ssce_subjects[subject].score:
			scores[subject] = True
		else:
			scores[subject] = False
	return scores