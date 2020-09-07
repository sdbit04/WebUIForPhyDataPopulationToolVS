from django import forms
from .models import Retails


class CreateRetail(forms.ModelForm):
    class Meta:
        model = Retails
        fields = [
            'name',
            'min_qualification'
        ]
