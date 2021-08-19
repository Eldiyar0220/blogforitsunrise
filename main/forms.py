from datetime import datetime

from django import forms

from .models import Post, Image, Comment


class PostForm(forms.ModelForm):
    created = forms.DateTimeField(initial=datetime.now().strftime('%Y-%m-%d %H:%M:%S'), required=False)
    class Meta:
        model = Post
        exclude = ('user', )

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image', )

#comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('user', 'post', 'active')