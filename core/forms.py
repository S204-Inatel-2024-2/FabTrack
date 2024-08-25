# core/forms.py
from django.core.exceptions import ValidationError
from django import forms
from .models import PrintModel

class PrintModelForm(forms.ModelForm):
    class Meta:
        model = PrintModel
        fields = ['model_name', 'stl_file', 'material', 'infill_percentage', 'layer_height']
    
    def clean_stl_file(self):
        file = self.cleaned_data.get('stl_file')
        if file:
            if not file.name.endswith('.stl'):
                raise ValidationError("Only STL files are allowed.")
        return file
