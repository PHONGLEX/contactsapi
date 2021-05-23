from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Contact
from .serializers import ContactSerializer


class ContactList(ListCreateAPIView):

    serializer_class = ContactSerializer
    permissions_classes = (permissions.IsAuthenticated,)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)


class ContactDetailView(RetrieveUpdateDestroyAPIView):

    serializer_class = ContactSerializer
    permissions_classes = (permissions.IsAuthenticated,)
    lookup_field = "id"

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(owner=self.request.user)