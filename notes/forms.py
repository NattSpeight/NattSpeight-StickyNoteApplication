from django import forms
from .models import Note, Post

class NoteForm(forms.ModelForm): #note form
    class Meta:
        model = Note
        fields = ['title', 'content']

class PostForm(forms.ModelForm): #Model form
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
