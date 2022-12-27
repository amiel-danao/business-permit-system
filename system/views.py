from django.shortcuts import render
from django.contrib.auth.decorators import login_required as login_required
from django.views.generic import ListView
from system.filters import BusinessPermitFilter
from system.forms import BusinessPermitForm
from system.models import BusinessPermit
from django.contrib.auth.mixins import LoginRequiredMixin
from django_tables2 import SingleTableView
from system.tables import BusinessPermitTable
from django_filters.views import FilterView


@login_required
def index(request):
    return render(request, template_name='system/home.html')


class BusinessPermitListView(LoginRequiredMixin, SingleTableView, FilterView):
    model = BusinessPermit
    table_class = BusinessPermitTable
    template_name = 'system/home.html'
    filterset_class = BusinessPermitFilter

    def get_context_data(self):
        context = super().get_context_data()
        context["form"] = BusinessPermitForm()
        return context