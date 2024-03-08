from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Conversation, Message
from products.models import Product

# Create your views here.

class ConversationList(ListView):
    model = Conversation
    context_object_name = 'conversations'
    template_name = 'messaging/conversation_list.html'

    def get_queryset(self):
        return Conversation.objects.filter(participants=self.request.user)

class ConversationDetail(DetailView):
    model = Conversation
    context_object_name = 'conversation'
    template_name = 'messaging/conversation_detail.html'
    pk_url_kwarg = 'conversation_id'

    def post(self, request, *args, **kwargs):
        """ POST Handling Logic """
        # Create a message related to the conversation
        conversation = self.get_object()
        message_text = request.POST.get('message')
        if message_text:
            Message.objects.create(
                conversation=conversation,
                sender=request.user,
                text=message_text
            )
            return redirect(conversation.get_absolute_url())
        else:
            # Handle the case where message is not valid
            return render(request, self.template_name, {
                'conversation': self.object,
                'error': 'Message text cannot be empty.'
            })

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Get the conversation object from the context
        conversation = context['conversation']
        # Add the message query set to the context
        context['messages'] = conversation.messages.order_by('sent_at')
        # Ensure to render product title in templates 
        context['product'] = conversation.product
        return context

class StartConversationView(LoginRequiredMixin, View):
    def get(self, request, product_slug):
        product = get_object_or_404(Product, slug=product_slug)
        defaults = {
            'topic': 'Product Inquiry',
            'status': 'Open'
        }
        # Check if a conversation exists or create a new one
        conversation, created = Conversation.objects.get_or_create(
            product=product,
            defaults=defaults
        )
        # Redirect to the conversation detail page
        return redirect('conversation_detail', conversation_id=conversation.id)

