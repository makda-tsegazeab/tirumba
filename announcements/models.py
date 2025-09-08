from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField  # For kebele_list (requires PostgreSQL)

VENUE_CHOICES = [
    ('st_mary_mekelle', 'St. Mary’s Church, Mekelle'),
    ('st_gabriel_axum', 'St. Gabriel’s Church, Axum'),
    # Add more Tigray churches/venues as needed
]

LANGUAGE_CHOICES = [
    ('am', 'Amharic'),
    ('ti', 'Tigrinya'),
    ('en', 'English'),
]

STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('approved', 'Approved'),
    ('sent', 'Sent'),
]

class Announcement(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True, blank=True)
    family_contact = models.CharField(max_length=20, null=True, blank=True)  # e.g., '+251912345678'
    venue = models.CharField(max_length=255, choices=VENUE_CHOICES)
    kebele_list = ArrayField(models.CharField(max_length=100), blank=True, default=list)  # e.g., ['Kebele 01', 'Kebele 02']
    date_of_funeral = models.DateTimeField()
    short_text = models.CharField(max_length=160)
    long_text = models.TextField()
    audio_url = models.URLField(null=True, blank=True)
    photo_url = models.URLField(null=True, blank=True)
    announcers = models.JSONField(default=dict, blank=True)  # e.g., [{"name": "Ato Abebe", "role": "Family"}]
    language = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='am')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_announcements')
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_announcements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    scheduled_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.venue} ({self.status})"

# Add other models later, e.g., Recipient
class Recipient(models.Model):
    phone = models.CharField(max_length=20, unique=True)
    kebele = models.CharField(max_length=100)
    opted_out = models.BooleanField(default=False)
    language_pref = models.CharField(max_length=5, choices=LANGUAGE_CHOICES, default='am')

    def __str__(self):
        return self.phone