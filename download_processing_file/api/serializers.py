from rest_framework import serializers
from file.models import File

class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField()
    processed = serializers.BooleanField(
        read_only = True
    )
    class Meta:
        model = File
        fields = ('id','file', 'uploaded_at', 'processed')