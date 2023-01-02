from django.contrib import admin

from system.models import Config

# Register your models here.
admin.site.site_header = "Dulag - Business Permit and License Registration System"
admin.site.site_title = "Dulag - Business Permit and License Registration System"
admin.site.index_title = "Welcome to admin portal"

@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    pass