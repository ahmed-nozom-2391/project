from rest_framework.generics import CreateAPIView
from django.db.models.query import EmptyQuerySet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import MyService
from user.models import MyUser
from .serializers import MyServiceSerializer
from .views import myservice_cart_context



class CartApi(CreateAPIView):
    serializer_class = MyServiceSerializer
    permission_classes = [IsAuthenticated]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # filter user services
        serializer.save(user=request.user)
        headers = self.get_success_headers(serializer.data)
        context = myservice_cart_context(request)
        context.update(serializer.data)
        return Response(context, status=status.HTTP_201_CREATED, headers=headers)
    

    
