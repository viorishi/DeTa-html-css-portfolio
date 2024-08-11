from django.shortcuts import render
from django.contrib.auth.models import User #ProjectSpecific
from rest_framework import generics #ProjectSpecific
from .serializers import UserSerializer, NoteSerializer #ProjectSpecific
from rest_framework.permissions import IsAuthenticated, AllowAny #ProjectSpecific
from .models import Note

class NoteListCreate(generics.ListCreateAPIView):#ProjectSpecific Create Note
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self): # Gets notes written per user
        user = self.request.user
        return Note.objects.filter(author=user)
    def perform_create(self, serializer): # Customize and validate
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView): #ProjectSpecific Delete Note
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView): #ProjectSpecific
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
