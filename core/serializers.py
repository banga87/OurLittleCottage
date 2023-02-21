from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import User


# Overriden UserCreateSerializer to control the POST request data
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ['id','username', 'password', 'email', 'first_name', 'last_name']