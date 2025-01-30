from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.contrib.auth.decorators import login_required


from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegistrationSerializer

from django.contrib.auth import authenticate



class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'message':'You have access!'})
 

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _= Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id':user.id})
        return Response(serializer.errors, status=400)
    


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            token, _= Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id':user.id})
        return Response({'error': 'Invalid credentials'}, status=401)




# def sign_in(request):
#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         confirm_password = request.POST.get('confirm_password')

#         # Password validation
#         if (
#             len(password) >= 8 and
#             re.search(r"[A-Z]", password) and
#             re.search(r"[a-z]", password) and
#             re.search(r"\d", password) and
#             re.search(r"[@$!%*_?&#]", password)
#         ):
#             if password == confirm_password:
#                 # Check if email or username already exists
#                 if User.objects.filter(email=email).exists():
#                     return JsonResponse({'error': f'"{email}" email already exists'}, status=400)
#                 elif User.objects.filter(username=username).exists():
#                     return JsonResponse({'error': f'"{username}" username already exists'}, status=400)
#                 else:
#                     # Create the user
#                     user = User.objects.create_user(
#                         email=email, 
#                         password=password, 
#                         username=username, 
#                         first_name=first_name, 
#                         last_name=last_name
#                     )
#                     user.save()
                    
#                     # Send email
#                     subject = f"New message from {name}"
#                     email_message = f"Name: {name}\nEmail: {email}\n\n{message}"
#                     from_email = settings.EMAIL_HOST_USER
#                     recipient_list = email  # Replace with your recipient email(s)

#                     try:
#                         send_mail(subject, email_message, from_email, recipient_list)
#                     except Exception as e:
#                         print(f"Error sending email: {e}")

#                     # Automatically log in the user and redirect to home page
#                     login(request, user)
#                     return JsonResponse({'redirect': '/'}, status=200)
#             else:
#                 return JsonResponse({'error': 'Both passwords do not match'}, status=400)
#         else:
#             return JsonResponse({'error': 'Password must match required format'}, status=400)
    
#     return JsonResponse({'error': 'Invalid request method.'}, status=405)

# # user auth system
# def log_in(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
        
#         # Authenticate the user
#         user = authenticate(username=username, password=password)
        
#         if user is not None:
#             login(request, user)
#             return JsonResponse({'redirect': '/'}, status=200)
#         else:
#             # Authentication failed
#             return JsonResponse({'error': 'Invalid username or password'}, status=400)
        
#     return JsonResponse({'error': 'Invalid request method.'}, status=405)

# # log out system
# @login_required
# def log_out(request):
    
    # logout(request)
    
    # return JsonResponse({'message': 'You have been logged out!'})