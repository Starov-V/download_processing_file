from rest_framework import status
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from .serializers import FileSerializer
from file.models import File
from file.tasks import processing
from django.db import transaction
from functools import partial

"""@api_view(['POST', 'GET'])
def upload(request):
    if request.method == 'POST':
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            processing.delay()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    files = File.objects.all()
    serializer = FileSerializer(files, many=True)
    return Response(serializer.data)
"""

#class FileList(generics.ListCreateAPIView):
#    queryset = File.objects.all()
#    serializer_class = FileSerializer

class FileList(APIView):

    def get(self, request):
        snippets = File.objects.all()
        serializer = FileSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = FileSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            transaction.on_commit(partial(processing.delay, file_id=instance.id))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
