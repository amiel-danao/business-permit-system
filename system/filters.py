import django_filters
from system.models import BusinessPermit

class BusinessPermitFilter(django_filters.FilterSet):
    reference_no = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = BusinessPermit
        fields = ['business_name', 'transaction_type', 'transaction_date', 'reference_no', 'status']