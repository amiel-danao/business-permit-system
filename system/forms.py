from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, Div, Field, HTML
from crispy_bootstrap5.bootstrap5 import FloatingField
from system.models import BusinessPermit

STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class BusinessPermitForm(forms.ModelForm):
    # business_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Business Name', 'class' : 'form-floating'}))
    # password = forms.CharField(widget=forms.PasswordInput())
    # address_1 = forms.CharField(
    #     label='Address',
    #     widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    # )
    # address_2 = forms.CharField(
    #     widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    # )
    # city = forms.CharField()
    # state = forms.ChoiceField(choices=STATES)
    # zip_code = forms.CharField(label='Zip')
    # check_me_out = forms.BooleanField(required=False)

    class Meta:
        model = BusinessPermit
        fields = '__all__'
        exclude = ('reference_no', )

    def __init__(self, *args, **kwargs):
        super(BusinessPermitForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        # self.helper["business_name"].wrap(Field, HTML(self.get_label('business_name', self.helper)))
        self.fields['community_tax_certificate'].label = "Community Tax Certificate(Cedula)"
        self.helper.layout = Layout(
            Row(
                Div(
                    HTML('<p class="business-form-section my-auto">Requirements</p>'),
                    css_class='col-12'),
                css_class='bordered-section'
            ),
            Row(
                Div(
                    Field("barangay_business_clearance"), 
                css_class='col-4'),
                Div(
                    Field("proof_of_business_name_registration"), 
                css_class='col-4'),
                Div(
                    Field("community_tax_certificate"), 
                css_class='col-4'),
                
                css_class='bordered-section'
            ),
            Row(
                Div(
                    HTML('<small class="text-center business-form-section my-auto">All other requirements required by law, ordinance and rules are subject to Post Audit Process</small>'),
                    css_class='col-12 text-center'),
                css_class='bordered-section'
            )
        )

        # You can dynamically adjust your layout
        # self.helper.layout.append(Button('next', 'Next Page', css_class='btn btn-success', type='button'))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('email', css_class='form-group col-md-6 mb-0'),
    #             Column('password', css_class='form-group col-md-6 mb-0'),
    #             css_class='form-row'
    #         ),
    #         'address_1',
    #         'address_2',
    #         Row(
    #             Column('city', css_class='form-group col-md-6 mb-0'),
    #             Column('state', css_class='form-group col-md-4 mb-0'),
    #             Column('zip_code', css_class='form-group col-md-2 mb-0'),
    #             css_class='form-row'
    #         ),
    #         'check_me_out',
    #         Submit('submit', 'Sign in')
    #     )