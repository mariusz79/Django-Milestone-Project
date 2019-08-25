from django import forms
from .models import Feature, FeatureComment

class FeatureForm(forms.ModelForm):
    """Created new feature"""
    class Meta:
        model = Feature
        fields = ('title', 'description', 'published_date')


class FeatureCommentForm(forms.ModelForm):
    """comment on feature"""
    text = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 200,
        'rows': 3,
        'style': 'width: 100%'
    }))

    class Meta:
        model = FeatureComment
        fields = ('text',)