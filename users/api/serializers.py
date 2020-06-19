from rest_framework.serializers import ModelSerializer, CharField, ValidationError

from django.contrib.auth.models import User


class UserLoginSerializer(ModelSerializer):
    """ Serializer for user login"""

    token = CharField(allow_blank=True, read_only=True)
    username = CharField()

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "token",
        ]
        extra_kwargs = {"password": {"write_only": True,}}

    def validate(self, data):
        """ Check user credentials """
        username = data["username"]
        password = data["password"]
        user = User.objects.filter(username=username).first()
        if not user:
            raise ValidationError("This username is not valid")
        if not user.check_password(password):
            raise ValidationError("Incorrect credential, please try again")
        data["token"] = "SOMERANDOMTOKEN"
        return data
