from rest_framework import serializers

#--------------MODELOS-----------
from Profile.models import ProfileModel, ProfileUser

class ProfileModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileModel
        fields = ('__all__')

class ProfileUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfileUser
        fields = ('__all__')
