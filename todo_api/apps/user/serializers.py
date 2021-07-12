from rest_framework import serializers
from django.contrib.auth.models import User
from .validators import (
    PasswordComplexityValidator,
    PasswordConfirmationValidator,
)


class UserSignUpSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        max_length=128, write_only=True, style={"input_type": "password"},
        label="Enter Password",
    )
    password2 = serializers.CharField(
        max_length=128, write_only=True, style={"input_type": "password"},
        label="Confirm Password",
    )

    class Meta:
        model = User
        fields = ["id", "username", "password1", "password2"]
        validators = [
            PasswordComplexityValidator(),
            PasswordConfirmationValidator(),
        ]

    def create(self, validated_data):
        username = validated_data.get("username")
        password1 = validated_data.get("password1")
        return User.objects.create_user(
            username=username,
            password=password1
        )


class AuthenticationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, write_only=True, style={"input_type": "password"}
    )

    class Meta:
        model = User
        fields = ["username", "password"]
