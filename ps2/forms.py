from django import forms
from ps2.models import Game


class GameModelForm(forms.ModelForm):

    class Meta:
        model = Game
        fields = '__all__'