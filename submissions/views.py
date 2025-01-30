from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings



from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import CustomForm
from .serializers import CustomFormSerializer, FormSubmissionSerializer


@csrf_exempt
def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not name or not email or not message:
            return JsonResponse({'error': 'All fields are required!'}, status=400)

        # Send email
        subject = f"New message from {name}"
        email_message = f"Name: {name}\nEmail: {email}\n\n{message}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = email  # Replace with your recipient email(s)

        try:
            send_mail(subject, email_message, from_email, recipient_list)
            return JsonResponse({'message': 'Form submitted and email sent successfully!'})
        except Exception as e:
            return JsonResponse({'error': f'Failed to send email: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)





class CustomFormView(APIView):
    def post(self, request):
        serializer = CustomFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FormSubmissionView(APIView):
    def post(self, request, slug):
        form = get_object_or_404(CustomForm, slug=slug)

        # Validate against the dynamic form's fields
        errors = {}
        data = request.data
        for field in form.fields:
            field_name = field['name']
            if field['required'] and field_name not in data:
                errors[field_name] = "This field is required."
        


        if errors:
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)

        # Save the submission
        submission_serializer = FormSubmissionSerializer(data={
            'form': form.id,
            'data': data
        })
        if submission_serializer.is_valid():
            submission_serializer.save()
            return Response({'message': 'Submission successful!'}, status=status.HTTP_201_CREATED)

        return Response(submission_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
