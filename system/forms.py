from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, Div, Field, HTML
from crispy_forms.bootstrap import PrependedText
from crispy_bootstrap5.bootstrap5 import FloatingField
from system.models import BusinessPermit
from django.utils.translation import gettext_lazy as _

PHONE_NUMBER_ATTRS = {'pattern': '[0][0-9]{10}', 'maxlength': '11'}

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

    class Meta:
        model = BusinessPermit
        fields = '__all__'
        exclude = ('reference_no', 'user', 'owners_gender', 'status', 'business_type')
        

    def __init__(self, *args, **kwargs):
        super(BusinessPermitForm, self).__init__(*args, **kwargs)
        
        self.helper = FormHelper(self)
        
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
        
        
        