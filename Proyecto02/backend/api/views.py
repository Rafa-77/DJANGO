from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    # Use def to overwrite specific methods
    
    # Only view notes written by you
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)
    
    # Manually check if all the fields are ok
    def perform_create(self, serializer):
        if serializer.is_valid():
            # Save the extra field of author
            serializer.save(author = self.request.user)
        else: 
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]
    
    # Only delete notes written by you
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author = user)

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
    
