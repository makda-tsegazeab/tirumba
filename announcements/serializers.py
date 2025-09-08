from rest_framework import serializers
from .models import Announcement, Recipient

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'created_by', 'approved_by']

    def validate_family_contact(self, value):
        if value and not value.startswith('+251'):
            raise serializers.ValidationError("Phone should start with +251")
        return value

    def create(self, validated_data):
        validated_data['created_by'] = self.context['request'].user
        return super().create(validated_data)

class RecipientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipient
        fields = '__all__'