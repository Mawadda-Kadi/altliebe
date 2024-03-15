from django.urls import path
from django.urls import reverse
from .views import ConversationList, ConversationDetail, StartConversationView
from products.models import Product


urlpatterns = [
    path('', ConversationList.as_view(), name='conversation_list'),
    path('start/<slug:product_slug>/', StartConversationView.as_view(), name='start_conversation'),
    path('conversation/<int:conversation_id>/', ConversationDetail.as_view(), name='conversation_detail'),
]
