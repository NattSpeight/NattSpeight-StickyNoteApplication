from django.test import TestCase
from django.urls import reverse
from .models import Note

class NoteModelTest(TestCase): #Tests if a note has the correct title and content

    def setUp(self):
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_title(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_content(self):
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')

class NoteViewTest(TestCase):

    def setUp(self):
        self.note = Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_list_view(self): # Test to ensure notes display correctly
        response = self.client.get(reverse('note_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_detail_view(self): # Test to see if note details are correctly shown
        response = self.client.get(reverse('note_detail', args=[self.note.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Note')

    def test_note_create_view(self): # Test to see if new note can be created sucessfully
        response = self.client.post(reverse('note_create'), {'title': 'New Note', 'content': 'New note content'})
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Note.objects.last().title, 'New Note')

    def test_note_edit_view(self): # Test to see if existing note can be changed
        response = self.client.post(reverse('note_edit', args=[self.note.id]), {'title': 'Updated Note', 'content': 'Updated note content'})
        self.assertEqual(response.status_code, 302)
        self.note.refresh_from_db()
        self.assertEqual(self.note.title, 'Updated Note')

    def test_note_delete_view(self): # Test to see if note can be deleted 
        response = self.client.post(reverse('note_delete', args=[self.note.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Note.objects.filter(id=self.note.id).exists())
