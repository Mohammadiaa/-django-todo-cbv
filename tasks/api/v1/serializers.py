from rest_framework import serializers
from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
     class Meta:
        model = Task
        fields = ["user", "title", "description", "is_done", "created_at", "updated_at"]
        read_only_fields = ['user', 'created_at', 'updated_at']