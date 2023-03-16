from django import forms
from .models import Stories


class StoryForm(forms.ModelForm):
    class Meta:
        model = Stories
        fields = ['tag']
