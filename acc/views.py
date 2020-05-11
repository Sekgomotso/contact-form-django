from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# home form function
def home_page(request):

    if request.method == 'POST':
        message = request.POST['about']

        send_mail('Registration form', 
         message,
         settings.EMAIL_HOST_USER, 
         ['wifow52238@inbov03.com'], 
         fail_silently=False )
    return render(request, 'acc/form.html')

# # thank you page
# def registered(request):
#     return render(request, 'acc/registered.html')

# from django.core import mail
# from django.template.loader import render_to_string
# from django.utils.html import strip_tags
# from django.conf import settings

# subject = 'Registration form'
# html_message = render_to_string('mail_form.html', {'context': 'values'})
# plain_message = strip_tags(html_message)
# from_email = settings.EMAIL_HOST_USER
# to = ['wifow52238@inbov03.com']

# mail.send_mail(subject, plain_message, from_email, [to], html_message=html_message)