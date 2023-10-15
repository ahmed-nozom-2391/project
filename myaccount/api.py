from rest_framework.generics import CreateAPIView
from django.db.models.query import EmptyQuerySet
from rest_framework.response import Response
from rest_framework import status
from .models import MyService
from user.models import MyUser
from .serializers import MyServiceSerializer




class CartApi(CreateAPIView):
    serializer_class = MyServiceSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
