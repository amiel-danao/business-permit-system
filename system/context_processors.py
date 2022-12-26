from django.contrib import admin


def global_context(request):
    return {
        'app_title': admin.site.site_title,
        'app_short_title': 'Dulag-Business Permit',
        'app_abbr': 'BPLS',
        'app_place': 'Dulag'
    }