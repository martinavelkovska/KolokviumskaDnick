from django.contrib import admin
from .models import Flight, Balloon, Airline, AirlinePilot, Pilot
# Register your models here.

class PilotAdmin(admin.ModelAdmin):
    list_display = ("ime", "prezime",)

class BalloonAdmin(admin.ModelAdmin):
    pass

class FlightAdmin(admin.ModelAdmin):
    exclude = ("user",)
    def has_add_permission(self, request, obj=None):
        if (obj and obj.user == request.user) or request.user.is_superuser:
            return True

    def has_change_permission(self, request, obj=None):
        if (obj and obj.user == request.user) or request.user.is_superuser:
            return True

    def has_delete_permission(self, request, obj=None):
        return False

    def save_model(self, request, obj, form, change):
        if obj is not None:
            obj.user = request.user

        super().save_model(request, obj, form, change)


class AirlinePilotAdmin(admin.TabularInline):
    model = AirlinePilot
    extra = 0

class AirlineAdmin(admin.ModelAdmin):
    list_display = ("ime",)
    inlines = [AirlinePilotAdmin]

admin.site.register(Pilot, PilotAdmin)
admin.site.register(Balloon, BalloonAdmin)
admin.site.register(Airline, AirlineAdmin)
admin.site.register(Flight, FlightAdmin)

