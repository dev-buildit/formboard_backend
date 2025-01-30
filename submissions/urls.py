from django.urls import path
from .views import CustomFormView, FormSubmissionView

urlpatterns = [
    path('api/forms/', CustomFormView.as_view(), name='create-form'),
    path('api/forms/<slug:slug>/', FormSubmissionView.as_view(), name='submit-form'),
]
