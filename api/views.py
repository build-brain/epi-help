from .serializers import *
from .models import *
from rest_framework import mixins
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


# class DiaryView

class ContactView(
        generics.ListAPIView,
        generics.CreateAPIView,
        generics.DestroyAPIView
    ):
    # permission_classes =[IsAuthenticated]
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        queryset = self.get_object(lookup_field)
        return self.destroy(request, *args, **kwargs)


# class ContactCreateView(generics.CreateAPIView):
#     # permission_classes =[IsAuthenticated]
#     # queryset = Contact.objects.create()
#     serializer_class = ContactSerializer
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)



class ContentView(generics.ListAPIView):
    # permission_classes =[IsAuthenticated]
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    


# TODO -------------- Type Trigger -----------------

class TypeTriggerView():
    serializer_class = TypeTriggerSerializer

    """
    def get(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    """


# TODO -------------- Type Seizure -----------------

class TypeSeizureView():
    serializer_class = TypeSeizureSerializer

    """
    def get(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    """


# TODO -------------- Type Aura --------------------

class TypeAuraView():
    serializer_class = TypeAuraSerializer

    """
    def get(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    """


# TODO -------------- Seizure ----------------------

class SeizureView():
    serializer_class = SeizureSerializer

    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    """


# TODO -------------- Aura -------------------------

class AuraView():
    serializer_class = AuraSerializer

    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    """

# TODO -------------- Report Event -----------------

class ReportEventView():
    serializer_class = ReportEventSerializer

    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    """

# TODO -------------- Content ----------------------

class ContentView():
    serializer_class = ContentSerializer

    """
    def get(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    """


# TODO -------------- Contact ----------------------

class ContactView():
    serializer_class = ContactSerializer

    """
    def get(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    """


# TODO -------------- General Settings -------------

class GeneralSettingsView():
    serializer_class = GeneralSettingsSerializer

    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    """

# TODO -------------- My Profile -------------------

class MyProfileView():
    serializer_class = MyProfileSerializer

    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    """

