from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):

	user = serializers.HiddenField(default=serializers.CurrentUserDefault())
	
	class Meta:
		model = ToDo
		fields = ["id", "title", "description", "created_at", "user"]