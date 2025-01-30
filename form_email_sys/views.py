from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']


        send_mail(
            'Contact Form',
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
    return render(request, "index.html")


# import smtplib

# try:
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.starttls()
#     server.login('daviddominic767@gmail.com', 'amdp yjzb nrbu voun')
#     print("Connected successfully!")
#     server.quit()
# except Exception as e:
#     print(f"Error: {e}")
