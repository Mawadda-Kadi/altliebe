from django.urls import path
from .views import ConversationListView, ConversationDetailView

urlpatterns = [
    path('', ConversationListView.as_view(), name='conversation_list'),
    path('<slug:conversation_slug>/', ConversationDetailView.as_view(), name='conversation_detail'),
]