from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('category','title','text','reference')
        # unique_together = ("author", "title")
    


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text',)
