from django.contrib import admin

from system.models import DEFAULT_MAYOR_FULL_NAME, DEFAULT_MAYOR_SIGNATURE, Config


def global_context(request):
    return {
        'app_title': admin.site.site_title,
        'app_short_title': 'Dulag-Business Permit',
        'app_abbr': 'BPLS',
        'app_place': 'Dulag'
    }


