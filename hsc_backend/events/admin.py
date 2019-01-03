from django.contrib import admin
from .models import Event, Tag, Host, Subscriber
# Register your models here.


class EventAdmin(admin.ModelAdmin):
    pass


class TagAdmin(admin.ModelAdmin):
    pass


class HostAdmin(admin.ModelAdmin):
    pass


class SubscriberAdmin(admin.ModelAdmin):
    pass


admin.site.register(Event, EventAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
