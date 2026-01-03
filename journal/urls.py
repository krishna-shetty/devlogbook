from django.urls import path
from .views import HomeView, EntryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('entries/<int:pk>', EntryView.as_view(), name='entry-detail'),
]
