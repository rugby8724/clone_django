from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    # In object - oriented programming, a metaclass is a class whose instances are classes.Just as an ordinary class
    # defines the behavior of certain objects, a metaclass defines the behavior of certain classes and their
    # instances.Not all object-oriented programming languages support metaclasses.
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
