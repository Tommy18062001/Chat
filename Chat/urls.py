from django.urls import path
from .views import ChatListView, ChatCreateView
app_name = 'chat'

urlpatterns = [
    path('', ChatListView.as_view(), name='all'),
    path('new/', ChatCreateView.as_view(), name='new'),
]
