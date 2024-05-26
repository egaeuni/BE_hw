from django import forms
from .models import Post

class listForm(forms.ModelForm):
    title = forms.CharField(label = '')
    content = forms.CharField(widget=forms.Textarea, label='')

    class Meta:
        model = Post
        fields = ['title', 'content']