from django.urls import path
from api.views import *
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('content/', ContentView.as_view(), name='content'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('contact/<int:pk>', ContactView.as_view(), name='contact')
]

# router = DefaultRouter()
# router.register(r'content', ContentView),
# router.register(r'contact', ContactView),
# urlpatterns = router.urls