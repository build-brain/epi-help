from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# --------------------------------------------------------------
class TypeSeizureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeSeizure
        fields = []


class SeizureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seizure
        fields = []


class TypeAuraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeAura
        fields = []


class AuraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aura
        fields = []


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = []


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = []