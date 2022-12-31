import django_tables2 as tables
from system.models import BusinessPermit
from django.utils.translation import gettext_lazy as _


class BusinessPermitTable(tables.Table):
    class Meta:
        model = BusinessPermit
        template_name = "django_tables2/bootstrap4.html"
        fields = ("business_name", "transaction_type", "transaction_date",
                  "reference_no", "status")
        empty_text = _("No applications found")
        attrs = {'class': 'table table-hover shadow records-table'}
        row_attrs = {'data-href': lambda record: record.get_absolute_url}