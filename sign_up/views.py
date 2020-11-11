from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status

from django.contrib.auth.models import User

from rest_auth.registration.views import RegisterView

class SignUpModelView(RegisterView):
    def post(self, request,  *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context = {'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.save(self.request)
        token, created = Token.objects.get_or_create(user=user)
        return Response(self.get_response_data(user),
                status=status.HTTP_201_CREATED)