from django import forms
from .models import PrintModel

class PrintModelForm(forms.ModelForm):
    class Meta:
        model = PrintModel
        fields = ['model_name', 'stl_file', 'material', 'infill_percentage', 'layer_height']
