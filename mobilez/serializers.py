from rest_framework import serializers
from .models import TodoMobilez

class TodoMobilezSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoMobilez
        fields = ["mobile", "completed", "timestamp", "updated", "user"]