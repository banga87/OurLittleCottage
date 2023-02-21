from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import User

"""
Overriden UserCreateSerializer to control the POST request data.
Ensuring we capture and send email, which is has a UNIQUE constraint.
"""
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        model = User
        fields = ['id','username', 'password', 'email', 'first_name', 'last_name']