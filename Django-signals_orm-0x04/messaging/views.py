from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()

# -------------------------------
# Delete user account
# -------------------------------
@login_required
def delete_user(request):
    """
    Allows the logged-in user to delete their account.
    Triggers post_delete signal to clean up related data.
    """
    user = request.user
    user.delete()
    return redirect('home')


# -------------------------------
# Inbox view showing only unread messages
# -------------------------------
@login_required
def inbox(request):
    """
    Displays only unread messages for the logged-in user.
    Uses the custom UnreadMessagesManager and .only() optimization.
    """
    unread_messages = Message.unread.for_user(request.user)
    return render(request, 'inbox.html', {'messages': unread_messages})
