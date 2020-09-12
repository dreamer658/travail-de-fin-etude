from django import forms
from moon.models.profile import Comment

class ComForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['description']
