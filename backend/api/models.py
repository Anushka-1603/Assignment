from django.db import models

class Reminder(models.Model):
    # date, time, message content, option to remind: SMS/Email
    
    CHOICE  = [
        ('email', 'Email'),
        ('sms', 'SMS'),
    ]
    
    date = models.DateField()
    time = models.TimeField()
    message = models.CharField(max_length=255)
    remind_via = models.CharField(max_length=5, choices=CHOICE)