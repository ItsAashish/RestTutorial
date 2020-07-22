from . import models
from rest_framework import serializers

class NameSerializer(serializers.Serializer):
    """ Serializers for testing basic APIview  """
    name = serializers.CharField(max_length = 10)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id','email', 'name', 'password',)
        extra_kwargs = {
            "password": {
                "write_only"    : True,
                "style"         : {
                    "input_type": "password"
                }      
            }
        }
    def create(self, validated_data):
        """ Creates and returns a User """
        user = models.UserProfile.objects.create_user(
            name        = validated_data['name'],
            email       = validated_data['email'],
            password    = validated_data['password']

        )
        return user


class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serializes Profile Feed"""
    class Meta:
        model = models.ProfileFeed
        fields = ('id' , 'user_profile' , 'status_text', 'date_created')
        extra_kwargs = {
            'user_profile' : {
                'read_only' : True
            }
        }
