from django.urls import path
from .views import ContactListCreateAPIView, ContactRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('contacts/', ContactListCreateAPIView.as_view(), name='contact-list-create'),
    path('contacts/<int:id>/', ContactRetrieveUpdateDestroyAPIView.as_view(), name='contact-detail'),
]
