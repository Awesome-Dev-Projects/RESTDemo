import email
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer as JWTTokenObtainPairSerializer


class CustomTokenObtainPairSerializer(JWTTokenObtainPairSerializer):
    username_field = get_user_model().USERNAME_FIELD


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'full_name')
        extra_kwargs = {
            "email": {
                "validators": [],
            },
        }

    # def validate(self, attrs):
    #     email=attrs['email']
    #     if email=='':
    #         print('email is empty')
    #         raise serializers.ValidationError('Email is required')
    #     if get_user_model().objects.filter(email).exists():
    #         raise serializers.ValidationError(
    #             f"Email {attrs['email']} is already taken")
    #     return attrs

    def validate_email(self, value):
        if not value or not value.strip() or value.strip() == '':
            raise serializers.ValidationError('Email is required')
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError('Email is already taken')
        if not value or '@' not in value or '.' not in value or value.count('@') > 1:
            raise serializers.ValidationError('Valid Email is required')
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                'Length of password must be at least 8 characters')
        return value

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user
