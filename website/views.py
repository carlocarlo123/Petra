from django.shortcuts import render
from django.core.mail import send_mail
from django.template import loader

def home(request):
	return render(request,'home.html',{})

def about_us(request):
	return render(request,'about_us.html',{})

def services(request):
	return render(request,'Services.html',{})

def industries(request):
	return render(request,'Industries.html',{})


def packages(request):
	return render(request,'packages.html',{})

def latest_news(request):
	return render(request,'latest_news.html',{})

def contact_us(request):
	if request.method=="POST":
		#grabbing data from the form
		name=request.POST['name']
		email_address=request.POST['name-email']
		mobile_number=request.POST['name-mobile']
		text_area=request.POST['textarea']
		diction={'name':name ,'email_address':email_address,
		'mobile_number':mobile_number,
		'text_area':text_area}


		#send email()
		send_mail(
			'Dear '+ name,
			'From : ' + str(email_address) +'\n' + #subject 
			 text_area, 
			 email_address,
			 ['carloab39@gmail.com'], 
			fail_silently=True, # to email
			)
		return render(request,'contact-us.html',{'email_address':email_address,'name':name})
		
	else:

		return render(request,'contact-us.html',{})

def blog(request):
	return render(request,'blog.html',{})

def Gallery(request):
	return render(request,'Gallery.html',{})





