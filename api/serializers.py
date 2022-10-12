from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import (
    TypeSeizure,
    Seizure,
    TypeAura,
    Aura,
    Content,
    Contact
)


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
        fields = ['name', 'descriptions']


class SeizureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seizure
        fields = [
            'when',
            'duration',
            'trigger',
            'descriptions_trigger',
            'type',
            'comment'
        ]


class TypeAuraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeAura
        fields = ['name', 'descriptions']


class AuraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aura
        fields = [
            'when',
            'duration',
            'trigger',
            'descriptions_trigger',
            'type',
            'comment'
        ]


class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = ['header', 'text', 'date', 'image']


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'disable_contact', 'phone_namber']