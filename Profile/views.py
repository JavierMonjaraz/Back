from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
import json

#--------------MODELOS-----------
from Profile.models import ProfileModel, ProfileUser

#--------------Serializers--------
from Profile.serializers import ProfileModelSerializers, ProfileUserSerializers

#--------------View--------------------
class ProfileModelView(APIView):
    def post(self, request, format=None):
        serializer=ProfileModelSerializers(data=request.data, context = {'request':request}) #Va a invocar a una clase de serializer
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response("Error formato")

class ProfileUserView(APIView):
    def post(self, request, format=None):
        serializer=ProfileUserSerializers(data=request.data, context={'request:':request})
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response('Error formato')

    def get(self, request, format=None):
        users = ProfileUser.objects.all()
        serializer = ProfileUserSerializers(users, many=True)
        return Response(serializer.data)

class ProfileUserViewByID(APIView):
    def get_object(self, pk):
        try:
            return ProfileUser.objects.get(pk=pk)
        except ProfileUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ProfileUserSerializers(user)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = ProfileUserSerializers(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
