from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

# -------------------------------
# Delete user account
# -------------------------------
@login_required
def delete_user(request):
    """
    View that allows the logged-in user to delete their own account.
    Deletes the user, which triggers the post_delete signal to clean up related data.
    """
    user = request.user
    user.delete()  # Triggers post_delete signal
    return redirect('home')  # Redirect to home page after deletion
