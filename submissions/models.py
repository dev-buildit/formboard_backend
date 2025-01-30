from django.db import models

# Create your models

# Form creation models

class CustomForm(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    fields = models.JSONField()
    created_at = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.title 
    

# Model for form submissions
class FormSubmission(models.Model):
    form = models.ForeignKey(CustomForm, related_name='submissions' ,on_delete=models.CASCADE)
    data = models.JSONField()
    sumitted_at = models.DateTimeField(auto_now_add=False)


    def __str__(self):
        return f'Submission for {self.form.title} at {self.sumitted_at}'