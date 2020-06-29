from django.shortcuts import render
from rest_framework import generics

#  Mixin that allows to create multiple objects from lists
from wonder.models import Users
from wonder.serializer import UserSerializer


class CreateListModelMixin(object):
    def get_serializer(self, *args, **kwargs):
        """ If an array is passed, set the serializer to many"""
        if isinstance(kwargs.get('data', {}), list):
            kwargs['many'] = True
        return super(CreateListModelMixin, self).get_serializer(*args, **kwargs)


class UserCreateView(CreateListModelMixin, generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer


class UserListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
