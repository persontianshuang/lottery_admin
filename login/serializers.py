from rest_framework import serializers
from base_model.models import User

from rest_framework.validators import UniqueValidator


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # field = '__all__'
        fields = ("username","password")

class UserRegSerializer(serializers.ModelSerializer):

    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])

    password = serializers.CharField(
        style={'input_type': 'password'},help_text="密码", label="密码", write_only=True,
    )


    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        return attrs

    class Meta:
        model = User
        fields = ("username","password")


