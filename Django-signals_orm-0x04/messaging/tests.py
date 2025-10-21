from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification


class MessageSignalTest(TestCase):
    def setUp(self):
        self.sender = User.objects.create_user(username='alice', password='pass')
        self.receiver = User.objects.create_user(username='bob', password='pass')

    def test_notification_created_when_message_sent(self):
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            content='Hello Bob!'
        )
        self.assertTrue(Notification.objects.filter(user=self.receiver, message=message).exists())
