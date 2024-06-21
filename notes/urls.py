from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line
    path('notes/', views.note_list, name='note_list'),
    path('note/<int:pk>/', views.note_detail, name='note_detail'),
    path('note/new/', views.note_create, name='note_create'),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('note/<int:pk>/delete/', views.note_delete, name='note_delete'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_create, name='post_create'),
]


# All URLs for both the Posts and Notes are listed here. 
# For example http://127.0.0.1:8000/note/new/ is used with 'note_create'