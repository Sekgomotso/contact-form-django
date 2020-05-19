from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

# home form function
def home_page(request):

    if request.method == 'POST':

        # Get user info
        name = request.POST["fname"]
        surname = request.POST["lname"]
        career = request.POST["career"]
        bio = request.POST["about"]

        send_mail('Registration form', 
         'First name: ' + name + '\n' + 'Last name: ' + surname + '\n' + 'Choice: ' + career + '\n' + 'About user: ' + bio,
         settings.EMAIL_HOST_USER, 
         ['jifica2667@chordmi.com'], 
         fail_silently=False )
    return render(request, 'acc/form.html')
