from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id', 'name', 'description', 'course',
            'semester', 'email', 'github_url', 'linkedin_url', 'image_url',
        ]