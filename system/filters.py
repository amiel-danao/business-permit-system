import django_filters
from system.models import BusinessPermit

class BusinessPermitFilter(django_filters.FilterSet):
    class Meta:
        model = BusinessPermit
        fields = ['status']