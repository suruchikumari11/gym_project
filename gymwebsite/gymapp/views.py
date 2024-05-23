from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import *
from . models import Member,No_of_people,Membershiptype,Contact
from datetime import datetime,timedelta

# Create your views here.


def login_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username exists
		if not User.objects.filter(username=username).exists():
			# Display an error message if the username does not exist
			messages.error(request, 'Invalid Username')
			return redirect('login_page')
		
		# Authenticate the user with the provided username and password
		user = authenticate(username=username, password=password)
		
		if user is None:
			# Display an error message if authentication fails (invalid password)
			messages.error(request, "Invalid Password")
			return redirect('login_page')
		else:
			# Log in the user and redirect to the home page upon successful login
			login(request, user)
			return redirect('home')
	
	# Render the login page template (GET request)
	return render(request, 'auth/login.html')

def profile(request):
	yourplans = Member.objects.filter(user=request.user)
	return render(request,'app/profile.html',{'allplans':yourplans})


def logout_view(request):
    logout(request)

    
    return redirect('login_page')

# Define a view function for the registration page
def register_page(request):
	# Check if the HTTP request method is POST (form submission)
	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		# Check if a user with the provided username already exists
		user = User.objects.filter(username=username)
		
		if user.exists():
			# Display an information message if the username is taken
			messages.info(request, "Username already taken!")
			return redirect('register')
		
		# Create a new User object with the provided information
		user = User.objects.create_user(
			first_name=first_name,
			last_name=last_name,
			username=username
		)
		
		# Set the user's password and save the user object
		user.set_password(password)
		user.save()
		
		# Display an information message indicating successful account creation
		messages.info(request, "Account created Successfully!")
		return redirect('login_page')
	
	# Render the registration page template (GET request)
	return render(request, 'auth/register.html')


def home(request):
    return render(request,'app/home.html')
    
def gallery(request):
    return render(request,'app/gallery.html')

def wellness(request):

	return render(request,'app/wellness.html')

def about(request):
	return render(request ,'app/about.html')

def personal(request):
	return render(request,'app/personal.html')

def contact(request):
	if request.method == 'POST':
		name = request.POST.get('name','')
		phone = request.POST.get('phone','')
		message = request.POST.get('message','')
		if request.user.is_authenticated:
			Contact.objects.create(user = request.user , name = name , phone = phone , message = message )
			return redirect('home')


	return render(request,'app/contact.html')	

def group(request):
	return render(request,'app/group.html')

def admin(request):
	return redirect('admin')

def showplan(request):
	membership_name = request.GET.get('name','')
	if membership_name == 'wellness':
		filtered_object = Membershiptype.objects.filter(type = membership_name)
		return render(request,'app/showplans.html',{'allplans':filtered_object,'membership_name':membership_name})
	elif membership_name == 'group':
		filtered_object = Membershiptype.objects.filter(type = membership_name)
		return render(request,'app/showplans.html',{'allplans':filtered_object,'membership_name':membership_name})
	elif membership_name == 'personal':
		filtered_object = Membershiptype.objects.filter(type = membership_name)
		return render(request,'app/showplans.html',{'allplans':filtered_object,'membership_name':membership_name})
	return render(request,'app/showplans.html')

def buymembershipform(request):
	M = request.GET.get('name','')	
	plan = request.GET.get('plan','')	
	validity = request.GET.get('validity','')

	
	if request.method == 'POST':
		membername = request.POST.get('membername','')
		memberemail = request.POST.get('memberemail','')
		memberphone = request.POST.get('memberphone','')
		memberdob = request.POST.get('memberdob','')
		membertiming = request.POST.get('membertiming','')
		membershiptype = request.POST.get('membershipname','')
		memberaddress = request.POST.get('memberaddress','')
		membershipplan = request.POST.get('membershipplan','')
		membershipvalidity = request.POST.get('membershipvalidity','')
		date_obj = datetime.strptime(memberdob, '%Y-%m-%d')
		formatted_date = date_obj.strftime('%Y-%m-%d')

		join_date_obj = datetime.now()
		
		if request.user.is_authenticated:
			user = request.user


			if membershipvalidity == '1 month':
				expire_date = join_date_obj + timedelta(days=30)
			elif membershipvalidity == '3 month':
				expire_date = join_date_obj + timedelta(days=90)
			elif membershipvalidity == '6 month':
				expire_date = join_date_obj + timedelta(days=180)
			elif membershipvalidity == '9 month':
				expire_date = join_date_obj + timedelta(days=270)
			elif membershipvalidity == '1 year':
				expire_date = join_date_obj + timedelta(days=360)
			else:
				expire_date = None


			


			Member.objects.create(
				user=user,
				name=membername,
				email=memberemail,
				phone=memberphone,
				dob=formatted_date,
				membershipname=membershiptype,
				address=memberaddress,
				timeslot=membertiming,
				price=membershipplan,
				validity=membershipvalidity,
				expire_date = expire_date
			)
			no_of_people = 1
			if no_of_people <=15:
				T = No_of_people.objects.filter(membershiptype=membershiptype,time=membertiming)
				if not T.exists():
					No_of_people.objects.create(user=user,membershiptype=membershiptype,time=membertiming,noofpeople=no_of_people)
				else:
					existing_object = T.first()
					existing_object.noofpeople += 1
					existing_object.save()
		return redirect('home')
		
						
	T = No_of_people.objects.filter(membershiptype=M)
	


	
			
	return render(request,'app/buymembershipform.html',{"M":M,'seat':T,'P':plan,'validity':validity})



