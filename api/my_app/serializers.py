from rest_framework import serializers
from .models import Snippet
# from rest_framework.authtoken.models import Token

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = '__all__'


# token = Token.objects.create(user=...)
# print(token.key)