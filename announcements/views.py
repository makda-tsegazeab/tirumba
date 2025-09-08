from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Announcement, Recipient
from .serializers import AnnouncementSerializer, RecipientSerializer

class AnnouncementViewSet(viewsets.ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    @action(detail=True, methods=['post'])
    def approve(self, request, pk=None):
        announcement = get_object_or_404(Announcement, pk=pk)
        if announcement.status != 'draft':
            return Response({'error': 'Only drafts can be approved'}, status=400)
        announcement.status = 'approved'
        announcement.approved_by = request.user
        announcement.save()
        # TODO: Queue TTS if no audio
        return Response({'status': 'approved'})

    @action(detail=True, methods=['post'])
    def dispatch(self, request, pk=None):
        announcement = get_object_or_404(Announcement, pk=pk)
        if announcement.status != 'approved':
            return Response({'error': 'Only approved can be dispatched'}, status=400)
        # TODO: Celery dispatch task
        return Response({'status': 'dispatch queued'})

class RecipientViewSet(viewsets.ModelViewSet):
    queryset = Recipient.objects.all()
    serializer_class = RecipientSerializer
    permission_classes = [IsAuthenticated]