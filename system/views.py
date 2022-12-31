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
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin


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
    strict=False

    def get_queryset(self):
        qs = super().get_queryset()
        status = self.request.GET.get("status", None)
        if status is not None:
            qs = qs.filter(status=status)
        return qs

    def get_context_data(self, **kwargs):
        context = super(BusinessPermitListView, self).get_context_data(**kwargs)
        f = self.filterset_class(self.request.GET)
        context['filter'] = f
        table = self.table_class(f.qs)
        RequestConfig(self.request).configure(table)
        context['table'] = table
        
        return context

class BusinessPermitCreateView(LoginRequiredMixin, CreateView, SuccessMessageMixin):
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
        for error in form.errors:
            for key, value in form.fields[error].error_messages.items():
                messages.error(self.request, f'{form.fields[error].label} - {value}', extra_tags=f'{error}')
        return super().form_invalid(form)


class BusinessPermitDetailView(FormMixin, DetailView):
    template_name = 'system/detail.html'
    model = BusinessPermit
    form_class = BusinessPermitForm

    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(BusinessPermitDetailView, self).get_context_data(**kwargs)
        context['form'] = BusinessPermitForm(True, self.request.POST or None, self.request.FILES or None, instance=self.object)
        context['read_only'] = True
        return context
