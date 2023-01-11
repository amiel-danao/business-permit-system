from smtplib import SMTPDataError
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required as login_required
from django.views.generic import ListView
from system.filters import BusinessPermitFilter
from system.forms import BusinessPermitForm
from system.models import BusinessPermit, Status, TransactionType
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
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.views.generic import View
from xhtml2pdf import pisa
from django.db.models import Q
import urllib
from django.utils import timezone
from django.core.mail import send_mail


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
        if not self.request.user.is_superuser:
            qs = qs.filter(user=self.request.user)
        status = self.request.GET.get("status", None)
        if status is not None:
            qs = qs.filter(status=status)
        return qs

    def get_context_data(self, **kwargs):
        context = super(BusinessPermitListView, self).get_context_data(**kwargs)
        species=self.get_queryset()
        f = self.filterset_class(self.request.GET, queryset=species)
        context['filter'] = f
        table = self.table_class(f.qs)
        RequestConfig(self.request).configure(table)
        context['table'] = table

        context['total_applications'] = BusinessPermit.objects.all().count()
        context['denied_applications'] = BusinessPermit.objects.filter(status=Status.DENIED).count()
        context['issued_applications'] = BusinessPermit.objects.filter(status=Status.ISSUED).count()
        
        context['for_verification_count'] = BusinessPermit.objects.filter(status=Status.FOR_VERIFICATION).count()
        context['for_renewals_count'] = BusinessPermit.objects.filter(~Q(status=Status.ISSUED), transaction_type=TransactionType.RENEWAL).count()
        context['for_issuance_count'] = BusinessPermit.objects.filter(status=Status.FOR_ISSUANCE).count()
        
        page_status = self.request.GET.get('status', None)
        if page_status:
            context['page_status'] = int(page_status)
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
        form = BusinessPermitForm(True, self.request.POST or None, self.request.FILES or None, instance=self.object)
        context['form'] = form
        context['read_only'] = True
        context['page_status'] = form.instance.status
        return context


@login_required
def reject_application(request, pk):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    instance = get_object_or_404(BusinessPermit, pk=pk)
    instance.status = Status.DENIED
    instance.deny_reason = request.POST.get('deny_reason', '')
    instance.deny_remarks = request.POST.get('deny_remarks', '')
    instance.save()
    send_mail(
        'Business Permit - Process Update',
        compose_email(instance),
        request.user.email,
        [instance.user.email,],
        fail_silently=False,
    )
    return redirect_with_params('system:index', status='2')


@login_required
def approve_application(request, pk):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    instance = get_object_or_404(BusinessPermit, pk=pk)
    form = BusinessPermitForm(request.POST)
    for key, value in request.POST.items():
        if key in form.fields:
            field = form.fields[key]
            value_to_set = value
            if field.widget.input_type == 'date':
                value_to_set = None if value == '' else value
            setattr(instance, key, value_to_set)
    instance.status = Status.FOR_ASSESSMENT_OF_FEES
    instance.save()
    try:
        send_mail(
            'Business Permit - Process Update',
            compose_email(instance),
            request.user.email,
            [instance.user.email,],
            fail_silently=False,
        )
    except SMTPDataError:
        pass
    return redirect_with_params('system:index', status='1')


@login_required
def confirm_certificate(request, pk):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    instance = get_object_or_404(BusinessPermit, pk=pk)
    instance.status = Status.FOR_ISSUANCE
    instance.processing_fee = request.POST.get('processing_fee', 0)
    instance.business_permit_fee = request.POST.get('business_permit_fee', 0)
    instance.sticker_fee = request.POST.get('sticker_fee', 0)
    instance.date_of_issuance = timezone.now()
    instance.save()
    send_mail(
        'Business Permit - Process Update',
        compose_email(instance),
        request.user.email,
        [instance.user.email,],
        fail_silently=False,
    )
    return redirect_with_params('system:index', status='3')


@login_required
def confirm_issuance(request, pk):
    if request.method != 'POST':
        return HttpResponseBadRequest()
    
    instance = get_object_or_404(BusinessPermit, pk=pk)
    instance.status = Status.ISSUED
    instance.save()
    send_mail(
        'Business Permit - Process Update',
        compose_email(instance),
        request.user.email,
        [instance.user.email,],
        fail_silently=False,
    )
    return redirect_with_params('system:index', status='4')


def compose_email(instance):
    if instance.status == Status.DENIED:
        return f"""Dear {instance.business_applicant_name},

            We wanted to reach out to you regarding the status of your application form. Unfortunately, we have had to reject your application at this time due to {instance.deny_reason}.
        [Remarks]
        {instance.deny_remarks}

        We appreciate your interest and encourage you to apply again in the future, should a suitable opportunity arise. In the meantime, please don't hesitate to reach out if you have any questions or concerns.

        Thank you for your interest and we wish you the best of luck in your business.

        Sincerely,
        Dulag Leyte, Processing Staff"""
    elif instance.status == Status.FOR_ASSESSMENT_OF_FEES:
        return f"""
            Dear {instance.business_applicant_name},

                I am writing to request approval for a business permit for your company, {instance.business_name}, which will be located at {instance.address}.

            Our staff will further process your application, and we will send another email once it's done.

            Thank you for your interest.

            Sincerely,
            Dulag Leyte, Processing Staff"""
    elif instance.status == Status.FOR_ISSUANCE:
        total = sum([float(instance.processing_fee), float(instance.business_permit_fee), float(instance.sticker_fee)])
        return f"""
        Dear {instance.business_applicant_name},

            We are pleased to inform you that your business permit application has been approved.
            
        The permit total fee of ₱{total} has been processed and receipted.

        Congratulations on the approval of your business permit, and we look forward to supporting your business as it grows and thrives in our community.

        If you have any questions or need further assistance, please don't hesitate to contact our office.

        Sincerely,
        Dulag Leyte, Processing Staff"""
    elif instance.status == Status.ISSUED:
        f"""
        Dear {instance.business_applicant_name},

            I am writing to let you know that your business permit is now ready to be printed.

        Thank you for your patience during the review process. We are excited to see your business thrive in our community.

        If you have any questions or need further assistance, please don't hesitate to contact our office.

        Sincerely,
        Dulag Leyte, Processing Staff"""

    return ""


def redirect_with_params(viewname, **kwargs):
    """
    Redirect a view with params
    """
    rev = reverse(viewname)

    params = urllib.parse.urlencode(kwargs)
    if params:
        rev = '{}?{}'.format(rev, params)

    return HttpResponseRedirect(rev)