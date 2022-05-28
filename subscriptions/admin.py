from django.contrib import admin

from subscriptions.models import Subscription, SubscriptionType


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'type', 'created_at', 'updated_at', 'expires_at')
    list_display_links = ('created_at', 'updated_at', 'expires_at')
    search_fields = ('user', )
    list_filter = ('user', 'type')


class SubscriptionTypeAdmin(admin.ModelAdmin):
    list_display = ('title', )


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(SubscriptionType, SubscriptionTypeAdmin)
