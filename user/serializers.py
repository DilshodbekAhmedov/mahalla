from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from user.models import User


def password_validator(value):
    if len(value) < 8:
        raise ValidationError('Passwrod is bad')
    else:
        return True


class PasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=(password_validator, ),
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('password',)


class CheckUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=(password_validator, ),
        help_text='Leave empty if no change needed',
        style={'input_type': 'password', 'placeholder': 'Password'}
    )

    class Meta:
        model = User
        fields = ('username', 'password')


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        password = self.initial_data.get('passwrod', False)
        if not password:
            raise ValueError('error')
        instance = super().create(validated_data)
        instance.password = make_password(password)
        # instance.is_staff = True
        instance.save()
        return instance
    class Meta:
        model = User
        fields = 'first_name', 'last_name', 'email', 'username', 'is_active', 'birthday', 'phone', \
            'user_type', 'neighborhood', 'sector'
