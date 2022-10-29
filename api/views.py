from .serializers import *
from .models import *
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated



# TODO -------------- Type Trigger -----------------

class TypeTriggerView(ListCreateAPIView, RetrieveAPIView):
    # permission_classes =[IsAuthenticated]
    queryset = TypeTrigger.objects.all()
    serializer_class = TypeTriggerSerializer



# TODO -------------- Type Seizure -----------------

class TypeSeizureView(ListCreateAPIView, RetrieveAPIView):
    # permission_classes =[IsAuthenticated]
    queryset = TypeSeizure.objects.all()
    serializer_class = TypeSeizureSerializer
    


# TODO -------------- Type Aura --------------------

class TypeAuraView(ListCreateAPIView, RetrieveAPIView):
    # permission_classes =[IsAuthenticated]
    queryset = TypeAura.objects.all()
    serializer_class = TypeAuraSerializer

 
 
# TODO -------------- Seizure ----------------------

class SeizureView(ListCreateAPIView):
    # permission_classes =[IsAuthenticated]
    queryset = Seizure.objects.all()
    serializer_class = SeizureSerializer
 


# TODO -------------- Aura -------------------------

class AuraView(ListCreateAPIView):
    # permission_classes =[IsAuthenticated]
    queryset = Aura.objects.all()
    serializer_class = AuraSerializer



# TODO -------------- Report Event -----------------

class ReportEventView(CreateAPIView):
    # permission_classes =[IsAuthenticated]
    queryset = ReportEvent.objects.all()
    serializer_class = ReportEventSerializer



# TODO -------------- Content ----------------------

class ContentView(ListAPIView, RetrieveAPIView):
    # permission_classes =[IsAuthenticated]
    queryset = Content.objects.all().order_by('date').reverse()
    serializer_class = ContentSerializer
    


# TODO -------------- Contact ----------------------

class ContactView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    # permission_classes =[IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer



# TODO -------------- General Settings -------------

class GeneralSettingsView(UpdateAPIView):
    # permission_classes =[IsAuthenticated]
    queryset = GeneralSettings.objects.all()
    serializer_class = GeneralSettingsSerializer



# TODO -------------- My Profile -------------------

class MyProfileView(UpdateAPIView):
    # permission_classes =[IsAuthenticated]
    queryset = MyProfile.objects.all()
    serializer_class = MyProfileSerializer




