from django import forms
from .models import *
from pyuploadcare.dj.forms import ImageField

class LikesForm(forms.Form):
    class Meta:
        model = Image
        exclude = '__all__'

class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment