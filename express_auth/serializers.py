from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, label='Password', required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(
        write_only=True, label='Confirm password', required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['email', 'password', 'password2', 'phone', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

        def validate(self, validated_data):
            # username = validated_data['username']
            email = validated_data['email']
            password = validated_data['password']
            password2 = validated_data['password2']
            phone = validated_data['phone']
            first_name = validated_data['first_name']
            last_name = validated_data['last_name']
            if email and User.objects.filter(email=email).exists():
                raise serializers.ValidationError({'email': 'Email addresses must be unique.'})
            if validated_data['password'] != validated_data['password2']:
                raise serializers.ValidationError({'password': 'The two passwords differ.'})
            user = User(email=email, phone=phone, first_name=first_name, last_name=last_name)
            user.set_password(password)
            print(user)
            user.save()
            return user
