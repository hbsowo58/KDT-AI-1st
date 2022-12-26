from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class meta:
        model = Todo
        # fields = 
        exclude = ("created", )