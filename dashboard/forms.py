from django import forms
from django.core.exceptions import ValidationError
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['title', 'uploaded_file']

# bouncer against denial wallet attack,and putting limit for max doc size 5mb
    def clean_uploaded_file(self):
        file = self.cleaned_data.get('uploaded_file')

        if file.size > 35 * 1024 * 1024:
            raise ValidationError("This PDF is too large! Maximum allowed size is 35MB.")
            
        return file