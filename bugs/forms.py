from django import forms
from .models import Bug, BugComment

class BugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = ('title', 'description', 'tag', 'published_date')


class BugCommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 200,
        'rows': 3,
        'style': 'width: 100%'
    }))

    class Meta:
        model = BugComment
        fields = ('email', 'text',)