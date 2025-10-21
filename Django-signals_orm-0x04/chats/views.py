from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from messaging.models import Message

# -------------------------------
# Conversation view with caching
# -------------------------------
@login_required
@cache_page(60)  # Cache this view for 60 seconds
def conversation_view(request, user_id):
    """
    Displays all messages in a conversation with a specific user.
    Cached for 60 seconds to improve performance.
    """
    messages = Message.objects.filter(
        sender=request.user,
        receiver_id=user_id
    ).select_related('sender', 'receiver').prefetch_related('replies')

    return render(request, 'chats/conversation.html', {'messages': messages})
