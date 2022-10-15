from rest_framework import serializers
from .models import *

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
        fields = [
            'header', 
            'text', 
            'date', 
            'image'
        ]


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'first_name', 
            'last_name', 
            'disable_contact', 
            'phone_namber'
        ]
    

class GeneralSettingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'help_delay'  ,
            'phone_sensitivity' ,
            'watch_sensitivity' ,
            'above_beats' ,
            'bellow_beats' ,
            'audible_alarm' ,
            'repeat_alarm' ,
            'audible_message' ,
            'repeat_message' ,
        ]


class MyProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'first_name', 
            'last_name', 
            'disable_contact', 
            'phone_namber',
            'birthday' ,
            'weight' ,
            'blood_type' ,
            'allergy' ,
            'congenital_diseases' ,
            'acquired_diseases' ,
            'triggers',
        ]
