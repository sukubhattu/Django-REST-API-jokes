from rest_framework import serializers

from .models import Jokes


class JokesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jokes
        fields = ["id", "punchLine", "author", "createdDate"]
