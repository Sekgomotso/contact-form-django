from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

# home form function
def home_page(request):

    if request.method == 'POST':

        # Get user info
        name = request.POST["fname"]
        surname = request.POST["lname"]
        email = request.POST["email"]
        career = request.POST["career"]
        bio = request.POST["about"]

        # email details
        send_mail('Registration form', 
         'First name: ' + name + '\n' + 'Last name: ' + surname + '\n' + 'User email: ' + email + '\n' 'Choice: ' + career + '\n' + 'About user: ' + bio,
         settings.EMAIL_HOST_USER, 
         ['gohapi9096@etoymail.com'], 
         fail_silently=False)

        #  email sent message
        messages.success(request, 'Your details has been forwarded to our admin. We will get back to you!')

    else:
        messages.error(request, '')

    return render(request, 'acc/form.html')
