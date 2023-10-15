from rest_framework.generics import CreateAPIView
from django.db.models.query import EmptyQuerySet
from rest_framework.response import Response
from rest_framework import status
from .models import MyService
from user.models import MyUser
from .serializers import MyServiceSerializer




# class CartApi(CreateAPIView):
#     serializer_class = MyServiceSerializer
    
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
#     def get_queryset(self):
#         user  = self.request.user
#         user_cart_id = self.request.COOKIES.get('user_cart_id')
#         if user.is_authenticated:
#             return Order.objects.filter(user = user, confirmed = False)
#         if user_cart_id == None:
#             return EmptyQuerySet
#         return NonUserOrder.objects.filter(user_cart_id = user_cart_id)