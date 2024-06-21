from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Post, Author
from .forms import NoteForm, PostForm

def note_list(request): #lists all notes
    notes = Note.objects.all()
    return render(request, 'notes/note_list.html', {'notes': notes})

def note_detail(request, pk): #details of notes
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_create(request): # create a new note
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})

def note_edit(request, pk): #edit an existing note
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})

def note_delete(request, pk): #delete an existing note
    note = get_object_or_404(Note, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    return render(request, 'notes/note_confirm_delete.html', {'note': note})

def post_list(request): # list of all posts
    posts = Post.objects.all()
    return render(request, 'notes/post_list.html', {'posts': posts})

def post_detail(request, pk): #details of posts
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'notes/post_detail.html', {'post': post})

def post_create(request): #create a new post
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'notes/post_form.html', {'form': form})

def home(request):
    return render(request, 'notes/home.html')