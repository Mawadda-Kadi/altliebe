from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
from .models import Conversation


class ConversationListViewTest(TestCase):

    def setUp(self):
        # Create a user to be used as seller
        self.seller = User.objects.create_user(
            username='seller', password='12345')

        # Create a product with the seller assigned
        self.product = Product.objects.create(
            title='Product',
            description='Description',
            price=10,
            # Assign the created user as the seller
            seller=self.seller
        )

        # Create users for conversation
        self.user1 = User.objects.create_user(
            username='user1', password='12345')
        self.user2 = User.objects.create_user(
            username='user2', password='12345')

        # Create conversations and assign them to users
        self.conversation1 = Conversation.objects.create(product=self.product)
        self.conversation1.participants.add(self.user1)
        self.conversation2 = Conversation.objects.create(product=self.product)
        self.conversation2.participants.add(self.user2)


class ConversationDetailViewTest(TestCase):

    def setUp(self):
        # Create a user and set as seller
        self.seller = User.objects.create_user(
            username='seller', password='12345')
        self.user = User.objects.create_user(username='user', password='12345')

        # Create a product and assign the created seller
        self.product = Product.objects.create(
            title='Product',
            description='Description',
            price=10,
            # Assign the created user as the seller
            seller=self.seller
        )

        # Create a conversation for the product and add user as participant
        self.conversation = Conversation.objects.create(product=self.product)
        self.conversation.participants.add(self.user)

    def test_conversation_detail_view(self):
        self.client.login(username='user', password='12345')
        url = reverse('conversation_detail', args=[self.conversation.id])
        response = self.client.get(url)
        # Check if the conversation detail is displayed correctly
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['conversation'], self.conversation)

    def test_post_message_in_conversation(self):
        self.client.login(username='user', password='12345')
        url = reverse('conversation_detail', args=[self.conversation.id])
        message_text = 'Hello'
        response = self.client.post(url, {'message': message_text})
        # Check if the message was created
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.conversation.messages.count(), 1)
        self.assertEqual(self.conversation.messages.first().text, message_text)
