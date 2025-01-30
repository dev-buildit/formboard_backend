from rest_framework import serializers
from .models import CustomForm, FormSubmission

    

class CustomFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomForm
        fields = '__all__'
        read_only_fields = ['created_at']

    def validate_fields(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Fields must be a list of field definitions.")
        for field in value:
            if not all(key in field for key in ['name', 'type', 'required']):
                raise serializers.ValidationError("Each field must have 'name', 'type', and 'required' keys.")
        return value

class FormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormSubmission
        fields = ['id', 'form', 'data', 'submitted_at']
        read_only_fields = ['submitted_at']