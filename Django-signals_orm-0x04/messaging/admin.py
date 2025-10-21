from django.contrib import admin
from .models import Message, Notification, MessageHistory

# Inline to show message edit history in Message admin
class MessageHistoryInline(admin.TabularInline):
    model = MessageHistory
    extra = 0
    readonly_fields = ('old_content', 'edited_at')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'timestamp', 'edited')
    search_fields = ('sender__username', 'receiver__username')
    inlines = [MessageHistoryInline]  # ✅ Display edit history in admin


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'message', 'created_at', 'is_read')
    list_filter = ('is_read',)

