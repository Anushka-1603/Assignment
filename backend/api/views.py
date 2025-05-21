from django.shortcuts import render
from .serializers import ReminderSerializer
from .models import Reminder
from rest_framework import generics 

class ReminderListCreateAPIView(generics.ListCreateAPIView):
    
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    
class ReminderDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    lookup_field = 'pk'