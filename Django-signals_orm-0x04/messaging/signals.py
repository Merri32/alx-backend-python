from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Message, Notification, MessageHistory

# -------------------------------
# Notification when a new message
# -------------------------------
@receiver(post_save, sender=Message)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(user=instance.receiver, message=instance)

# -------------------------------
# Log old content before message edit
# -------------------------------
@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if not instance.pk:
        # New message, nothing to log
        return
    try:
        old_message = Message.objects.get(pk=instance.pk)
    except Message.DoesNotExist:
        return

    if old_message.content != instance.content:
        # Save old content to MessageHistory
        MessageHistory.objects.create(message=old_message, old_content=old_message.content)
        instance.edited = True  # Mark message as edited

# -------------------------------
# Delete all user-related data on account deletion
# -------------------------------
@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    # Delete messages where the user was sender or receiver
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    
    # Delete notifications belonging to the user
    Notification.objects.filter(user=instance).delete()
    
    # Delete message histories linked to messages of this user
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()
