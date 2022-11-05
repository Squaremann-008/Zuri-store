from django.shortcuts import render
from .models import Artiste, Song, Lyric
from .serializers import ArtisteSerializer, SongSerializer, LyricSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@api_view(['GET','PUT','DELETE'])
def musicapp_api(request):
    if request.method == 'GET':
        data = Song.objects.all()
        serializer = SongSerializer(data, context={'request': request}, many=True)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        Song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)