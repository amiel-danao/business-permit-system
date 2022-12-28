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
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.urls import reverse
from django_tables2.config import RequestConfig

@login_required
def index(request):
    return render(request, template_name='system/home.html')


class BusinessPermitListView(LoginRequiredMixin, SingleTableView, FilterView):
    model = BusinessPermit
    table_class = BusinessPermitTable
    template_name = 'system/home.html'
    filterset_class = BusinessPermitFilter
    table_pagination = {
        'per_page': 5,
    }

    def get_queryset(self):
        qs = super().get_queryset()
        status = self.request.GET.get("status", None)
        if status is not None:
            qs = qs.filter(status=status)
        return qs

class BusinessPermitCreateView(LoginRequiredMixin, CreateView):
    model = BusinessPermit
    # fields = '__all__'
    form_class = BusinessPermitForm
    template_name = 'system/home.html'

    def get_success_url(self):
        return reverse("system:index")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        # messages.error(self.request, self.error_message)
        return super().form_invalid(form)