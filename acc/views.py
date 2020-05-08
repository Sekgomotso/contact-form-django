from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# home form function
def home_page(request):

    if request.method == 'POST':
        message = request.POST['message']

        send_mail('Registration form', 
         message, 
         settings.EMAIL_HOST_USER, 
         ['wifow52238@inbov03.com'], 
         fail_silently=False )
    return render(request, 'acc/form.html')

# # thank you page
# def registered(request):
#     return render(request, 'acc/registered.html')
