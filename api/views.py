from django.shortcuts import render

from rest_framework import generics

from .models import Jokes
from .serializers import JokesSerializer

import random
from django.http import Http404


class JokesList(generics.ListAPIView):
    queryset = Jokes.objects.all()
    serializer_class = JokesSerializer


class JokeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jokes.objects.all()
    serializer_class = JokesSerializer


class JokeCreate(generics.CreateAPIView):
    queryset = Jokes.objects.all()
    serializer_class = JokesSerializer


class JokeRandom(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jokes.objects.all()
    serializer_class = JokesSerializer

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        count = queryset.count()
        randomPK = (random.randint(1, count))
        # make sure to catch 404's below
        try:
            obj = queryset.get(pk=randomPK)
            self.check_object_permissions(self.request, obj)
            return obj
        except Jokes.DoesNotExist:
            raise Http404
