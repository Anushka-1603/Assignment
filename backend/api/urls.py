from django.urls import path
from .views import ReminderListCreateAPIView, ReminderDetailAPIView

urlpatterns = [
    path('reminders/', ReminderListCreateAPIView.as_view()),
    path('reminders/<int:pk>/', ReminderDetailAPIView.as_view()),
]