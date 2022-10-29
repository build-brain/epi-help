from django.urls import path
from api.views import *
from rest_framework.routers  import SimpleRouter

urlpatterns = [
    
    path('type-trigger/', TypeTriggerView.as_view()),
    path('type-trigger/<int:pk>',TypeTriggerView.as_view()),

    path('type-seizure/', TypeSeizureView.as_view()),
    path('type-seizure/<int:pk>', TypeSeizureView.as_view()),
    path('seizure/',SeizureView.as_view()),
    path('seizure/<int:pk>',SeizureView.as_view()),

    path('type-aura/', TypeAuraView.as_view()),
    path('type-aura/<int:pk>', TypeAuraView.as_view()),
    path('aura/',AuraView.as_view()),
    path('aura/<int:pk>',AuraView.as_view()),

    path('content/', ContentView.as_view()),
    path('content/<int:pk>', ContentView.as_view()),

    path('contact/', ContactView.as_view()),
    path('contact/<int:pk>', ContactView.as_view()),

    path('general-settings/', GeneralSettingsView.as_view()),
    path('my-profile/', MyProfileView.as_view()),

]

# router = SimpleRouter()
# router.register('content/', ContentView),
# router.register('contact/', ContactView),
# router.register('contact/{pk}', ContactView),
# urlpatterns += router.urls
