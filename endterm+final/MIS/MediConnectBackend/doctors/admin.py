from django.contrib import admin
from .models import Doctor, Appointment

admin.site.register(Appointment)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['profile', 'specialty', 'clinic_location', 'license_status']
    list_filter = ['license_status']
    actions = ['verify_license', 'reject_license']

    def verify_license(self, request, queryset):
        queryset.update(license_status='Verified')
    verify_license.short_description = "Mark selected licenses as verified"

    def reject_license(self, request, queryset):
        queryset.update(license_status='Rejected')
    reject_license.short_description = "Mark selected licenses as rejected"