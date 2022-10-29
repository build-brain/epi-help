from rest_framework import serializers
from .models import *



# TODO -------------- Type Trigger -----------------

class TypeTriggerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeTrigger
        fields = '__all__'



# TODO -------------- Type Seizure -----------------

class TypeSeizureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeSeizure
        fields = ['name', 'descriptions']
    


# TODO -------------- Type Aura --------------------

class TypeAuraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TypeAura
        fields = ['name', 'descriptions']

 
 
# TODO -------------- Seizure ----------------------

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
 


# TODO -------------- Aura -------------------------

class AuraSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aura
        fields = [
            # 'when',
            'duration',
            'trigger',
            'descriptions_trigger',
            'type',
            'comment'
        ]



# TODO -------------- Report Event -----------------

class ReportEventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ReportEvent
        fields = '__all__'



# TODO -------------- Content ----------------------

class ContentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Content
        fields = [
            'header', 
            'text', 
            'date', 
            'image'
        ]
    


# TODO -------------- Contact ----------------------

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'first_name',
            'last_name',
            'disable_contact',
            'email',
            'phone_number'
        ]



# TODO -------------- General Settings -------------

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



# TODO -------------- My Profile -------------------

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
