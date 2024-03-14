from rest_framework import serializers
from django.conf import settings
from .models import *

# the image serializer is used to serialize nearly all images
# images are not just limited to reports
# images can also be used for forum posts 
class ImageSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields = ["id", 'title', 'image_url']

    def get_image_url(self, obj):
        if obj.file:
            return f"{settings.MEDIA_URL}{obj.file.name}"
        return None
    

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ["user", 
                  'title', 
                  'description', 
                  'images', 
                  'videos', 
                  "visible", 
                  'created_at']