from django import forms
from .models import Character

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = ['race', 'gender', 'character_class']
