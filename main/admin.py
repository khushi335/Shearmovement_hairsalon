from django.contrib import admin
from .models import About, TeamMember, Service, ServicePrice, GalleryImage

# Register your models here.
admin.site.register(About)
admin.site.register(Service)
admin.site.register(TeamMember)
admin.site.register(ServicePrice)

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at')