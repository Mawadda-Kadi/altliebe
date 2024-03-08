from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Conversation, Message

# Create your views here.

class ConversationListView(ListView):
    model = Conversation
    context_object_name = 'conversations'
    template_name = 'messaging/conversation_list.html'

    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)

class ConversationDetailView(DetailView):
    model = Conversation
    context_object_name = 'conversation'
    template_name = 'messaging/conversation_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'conversation_slug'


