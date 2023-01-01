from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, Div, Field, HTML
from crispy_forms.bootstrap import PrependedText
from crispy_bootstrap5.bootstrap5 import FloatingField
from system.models import BusinessPermit, YesNoChoice
from django.utils.translation import gettext_lazy as _
from system.models import BusinessType


PHONE_NUMBER_ATTRS = {'pattern': '[0][0-9]{10}', 'maxlength': '11'}
FILE_DOCUMENT_ONLY = 'application/msword, application/vnd.ms-excel, application/vnd.ms-powerpoint, text/plain, application/pdf, image/*'

class BusinessPermitForm(forms.ModelForm):
    business_contact_no = forms.CharField(widget=forms.TextInput(attrs=PHONE_NUMBER_ATTRS), label='Contact No.')
    tax_payer_contact_no = forms.CharField(widget=forms.TextInput(attrs=PHONE_NUMBER_ATTRS), label='Contact No.', required=False)
    sss_no = forms.RegexField(
        required=False,
        label='SSS No.',
        regex='^(?:\d{3}-\d{2}-\d{3})$',
        error_messages = {'invalid': _("Please follow the correct SSS No. format ex: AAA-GG-SSSS")})
    tin_no = forms.RegexField(
        required=False,
        label='TIN No.',
        regex='^(?:\d{3}-\d{3}-\d{3}|\d{3}-\d{3}-\d{3}-\d{3})$',
        error_messages = {'invalid': _("Please follow the correct TIN No. format ex: xxx-xxx-xxx")})

    community_tax_date_issued = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Date issued', required=False)

    philhealth_no = forms.RegexField(
        required=False,
        regex='^(?:\d{2}-\d{9}-\d{1})$',
        error_messages = {'invalid': _("Please follow the correct Philhealth No. format ex: xx-xxxxxxxxx-x")}, label='Philhealth No.')

    pagibig_no = forms.RegexField(
        required=False,
        regex='^(?:\d{12})$',
        error_messages = {'invalid': _("Please follow the correct Pag-ibig No. format ex: xxxxxxxxxxxx")}, label='Pag-ibig No.')

    rent_start = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Rent start(monthly/year)', required=False)

    barangay_business_clearance_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Date issued', required=False)
    location_zoning_clearance_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Date issued', required=False)
    health_clearance_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Date issued', required=False)
    occupancy_permit_clearance_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Date issued', required=False)
    fire_safety_inspection_clearance_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Date issued', required=False)
    police_clearance_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Date issued', required=False)
    others_clearance_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), label='Date issued', required=False)

    business_type = forms.TypedChoiceField(
        label = "Kind of ownership",
        choices = BusinessType.choices,
        widget = forms.RadioSelect(attrs={'class': 'form-check form-check-inline'}),
        initial = '1',
        required = True,
    )

    barangay_business_clearance = forms.FileField(widget=forms.FileInput(attrs={'accept': FILE_DOCUMENT_ONLY}), required=False)
    proof_of_business_name_registration = forms.FileField(widget=forms.FileInput(attrs={'accept': FILE_DOCUMENT_ONLY}), required=False)
    community_tax_certificate = forms.FileField(widget=forms.FileInput(attrs={'accept': FILE_DOCUMENT_ONLY}), required=False)


    class Meta:
        model = BusinessPermit
        fields = '__all__'
        exclude = ('reference_no', 'user', 'owners_gender', 'status', 'bfp_tracking_no', 'form_control_no', 
                    'deny_reason', 'deny_remarks', 'processing_fee', 'business_permit_fee', 'sticker_fee',
                    'date_of_issuance', 'business_identification_no', 'original_receipt_no')
        

    def __init__(self, read_only=False, *args, **kwargs):
        super(BusinessPermitForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        
        if read_only:
            for nam, field in self.fields.items():
                field.disabled = True
        
        self.helper.form_show_errors = True
        self.helper.error_text_inline = True
        
        self.fields['business_name'].label = False
        self.fields['employee_no_male'].label = False
        self.fields['employee_no_female'].label = False
        self.fields['employee_no_male_residing'].label = False
        self.fields['employee_no_female_residing'].label = False

        self.fields['code_1'].label = False
        self.fields['code_2'].label = False
        self.fields['code_3'].label = False
        self.fields['code_4'].label = False

        self.fields['line_of_business_1'].label = False
        self.fields['line_of_business_2'].label = False
        self.fields['line_of_business_3'].label = False
        self.fields['line_of_business_4'].label = False

        self.fields['receipts_1'].label = False
        self.fields['receipts_2'].label = False
        self.fields['receipts_3'].label = False
        self.fields['receipts_4'].label = False

        self.fields['subscribed_1'].label = False
        self.fields['subscribed_2'].label = False
        self.fields['subscribed_3'].label = False
        self.fields['subscribed_4'].label = False

        self.fields['paid_up_1'].label = False
        self.fields['paid_up_2'].label = False
        self.fields['paid_up_3'].label = False
        self.fields['paid_up_4'].label = False

        self.fields['owner_rented_name'].label = False
        self.fields['owner_rented_address'].label = False

        self.fields['barangay_business_clearance_date'].label = False
        self.fields['location_zoning_clearance_date'].label = False
        self.fields['health_clearance_date'].label = False
        self.fields['occupancy_permit_clearance_date'].label = False
        self.fields['fire_safety_inspection_clearance_date'].label = False
        self.fields['police_clearance_date'].label = False
        self.fields['others_clearance_date'].label = False

        self.fields['barangay_business_clearance_verified_by'].label = False
        self.fields['location_zoning_clearance_verified_by'].label = False
        self.fields['health_clearance_verified_by'].label = False
        self.fields['occupancy_permit_clearance_verified_by'].label = False
        self.fields['fire_safety_inspection_clearance_verified_by'].label = False
        self.fields['police_clearance_verified_by'].label = False
        self.fields['others_clearance_verified_by'].label = False

        # self.fields['processing_fee'].label = False
        # self.fields['business_permit_fee'].label = False
        # self.fields['sticker_fee'].label = False
        
        
        
        
        
        