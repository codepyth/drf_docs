from rest_framework import serializers
from .models import TodoMobilez

class TodoMobilezSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoMobilez
        fields = ["id", "mobile", "completed", "timestamp", "updated", "user"]