from django.shortcuts import render
from django.core.mail import send_mail
from  django.conf import settings
def Contact(request):
        if request.method == 'POST':
                send_mail(
			request.POST['subject'],
   			request.POST['message'],
			settings.EMAIL_HOST_USER,
			[request.POST['email']],
		)
        return render(request, 'contact/contact.html', {})
	