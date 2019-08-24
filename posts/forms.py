from django import forms
from .models import Post, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'published_date')

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 200,
        'rows': 3,
        'style': 'width: 100%'
    }))

    class Meta:
        model = Comment
        fields = ('text',)