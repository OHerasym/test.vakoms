from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from exuser.forms import MyRegistrationForm
from app1.models import UserProfile
from django.utils import timezone
import hashlib, datetime, random
import smtplib

#def send(request):
#	send_mail(('Subject here').encode('utf-8'), ('Here is the message.').encode('utf-8'), ('task.vakoms@gmail.com').encode('utf-8'),
#                [('oolleehh@gmail.com').encode('utf-8')], fail_silently=False)
#	return render(request, "home.html")

def home(request):
	return render(request, "home.html")

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def loggedin(request):
	return render_to_response('loggedin.html', 
		{'full_name': request.user.first_name})

def invalid_login(request):
	return render_to_response('invalid_login.html')

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	try:
		user=UserProfile.objects.get(email=username)
		pass
	except:
		return HttpResponseRedirect('/accounts/invalid')
	
	if user.is_active == False:
		return HttpResponseRedirect('/accounts/invalid')

	user = auth.authenticate(username=username, password=password)

	

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')

def register_success(request):
	return render_to_response('register_success.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')

def register_user(request):
	if request.method == 'POST':
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()

			username = form.cleaned_data['first_name']
			email = form.cleaned_data['email']
			#key
			salt = hashlib.sha1((str(random.random())).encode('utf-8')).hexdigest()[:5]
			activation_key = hashlib.sha1((salt+email).encode('utf-8')).hexdigest()
			key_expires = datetime.datetime.today() + datetime.timedelta(2)

            #Get user by username
			user=UserProfile.objects.get(email=email)
			user.activation_key = activation_key
			user.key_expires = key_expires
			user.save()
			#send mail
			sender = settings.EMAIL_HOST_USER
			receivers = [email, settings.EMAIL_HOST_USER]
			email_subject = u'Account confirmation'
			message = u"Hey %s, thanks for signing up. To activate your account, click this link within \
            48hours http://127.0.0.1:8000/accounts/confirm/%s" % (username, activation_key)
			body = '\r\n'.join(['To: %s' % receivers, 
				'From: %s' % sender, 'Subject: %s' % email_subject, '\n %s' % message])

			smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
			smtpObj.ehlo()
			smtpObj.starttls()
			smtpObj.login('task.vakoms@gmail.com', 'vakoms2015')
			smtpObj.sendmail(sender, receivers, body)
			smtpObj.quit() 

			return HttpResponseRedirect('/accounts/register_success')

	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()

	return render_to_response('register.html', args)


def register_confirm(request, activation_key):
	if request.user.is_authenticated():
		HttpResponseRedirect('/home')

	user_profile = get_object_or_404(UserProfile, activation_key=activation_key)
#
	if user_profile.key_expires < timezone.now():
		return render_to_response('confirm_expired.html')

	user_profile.is_active = True
	user_profile.save()

	return render_to_response('confirm.html')