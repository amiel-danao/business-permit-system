from django.db import models
from authentication.models import CustomUser
import random

GENDER = ('Male', 'Female')

def generate_ref_no() -> str:
    #REF-546200971
    uid = None
    existing_object = BusinessPermit.objects.all().first()
    while existing_object is not None or uid is None:
        uid = random.sample(range(1, 999999999), 1)
        uid = str(uid[0]).zfill(9)
        existing_object = BusinessPermit.objects.filter(reference_no=uid).first()
    return f'REF-{uid}'

class BusinessPermit(models.Model):
    class BusinessType(models.IntegerChoices):
        SOLE = 1, "Sole Proprietorship"
        ONE = 2, "One Person Corporation"
        PARTNERSHIP = 3, "Partnership"
        CORPORATION = 4, "Corporation"
        COOPERATIVE = 5, "Cooperative"
    class Gender(models.IntegerChoices):
        MALE = 1
        FEMALE = 2
    class Status(models.IntegerChoices):
        FOR_VERIFICATION = 1
        DENIED = 2
        FOR_ASSESSMENT_OF_FEES = 3
        FOR_ISSUANCE = 4
        ISSUED = 5
    class TransactionType(models.IntegerChoices):
        NEW_APPLICATION = 1
        RENEWAL = 2
        QUARTERLY = 3
        SEMI_ANNUAL = 4
        ANNUALY = 5
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE)

    business_name = models.CharField(blank=False, max_length=50, default='', unique=True)
    reference_no = models.CharField(blank=False, max_length=13, unique=True, default=generate_ref_no)

    business_type = models.PositiveSmallIntegerField(
        choices=BusinessType.choices,
        default=BusinessType.SOLE
    )

    status = models.PositiveSmallIntegerField(
        choices=Status.choices,
        default=Status.FOR_VERIFICATION
    )

    transaction_type = models.PositiveSmallIntegerField(
        choices=TransactionType.choices,
        default=TransactionType.NEW_APPLICATION
    )

    transaction_date = models.DateField(auto_now=True)

    barangay_business_clearance = models.FileField(upload_to ='requirements/%Y/%m/%d/', blank=True)
    proof_of_business_name_registration = models.FileField(upload_to ='requirements/%Y/%m/%d/', blank=True)
    community_tax_certificate = models.FileField(verbose_name="Community Tax Certificate(Cedula)", upload_to ='requirements/%Y/%m/%d/', blank=True)

    business_contact_no = models.CharField(verbose_name="Contact No.", max_length=11, default="", blank=True)

    business_house_no = models.CharField(verbose_name="House No./Bldg No.", max_length=40, default="", blank=True)
    business_street = models.CharField(verbose_name="Street Name", max_length=40, default="", blank=True)
    business_barangay = models.CharField(verbose_name="Barangay", max_length=40, default="", blank=False)

    tax_payer_surname = models.CharField(verbose_name="Surname", max_length=40, default="", blank=False)
    tax_payer_firstname = models.CharField(verbose_name="Firstname", max_length=40, default="", blank=False)
    tax_payer_middle_name = models.CharField(verbose_name="Middle Name", max_length=40, default="", blank=True)
    tax_payer_contact_no = models.CharField(verbose_name="Contact No.", max_length=11, default="", blank=True)

    tax_payer_house_no = models.CharField(verbose_name="House No./Bldg No.", max_length=40, default="", blank=True)
    tax_payer_street = models.CharField(verbose_name="Street Name", max_length=40, default="", blank=True)
    tax_payer_barangay = models.CharField(verbose_name="Barangay", max_length=40, default="", blank=False)
    tax_payer_city = models.CharField(verbose_name="City/Municipality", max_length=40, default="", blank=False)

    treasury_name = models.CharField(verbose_name="Name of President/Treasury of Corporation", max_length=40, default="", blank=False)
    sss_no = models.CharField(verbose_name="SSS. No.", max_length=11, blank=True)
    tin_no = models.CharField(verbose_name="TIN", max_length=15, blank=True)

    community_tax_certificate_no = models.CharField(verbose_name="Community Tax Certificate No.(Individual or Corporate)", max_length=30, blank=True)
    community_tax_date_issued = models.DateField(verbose_name="Date issued", blank=True, null=True)
    community_tax_place_issued = models.CharField(verbose_name="Place issued", max_length=50, blank=True)

    transfer_of_ownership_name = models.CharField(verbose_name="If transfer of ownership from whom acquired", max_length=50, blank=True)

    philhealth_no = models.CharField(verbose_name="Philhealth No.", max_length=14, blank=True)
    pagibig_no = models.CharField(verbose_name="Pag-ibig No.", max_length=12, blank=True)
    email = models.EmailField(verbose_name='Email Address', blank=True)

    employee_no_male = models.PositiveIntegerField(default=0)
    employee_no_female = models.PositiveIntegerField(default=0)

    code_1 = models.CharField(max_length=20, blank=True)
    code_2 = models.CharField(max_length=20,blank=True)
    code_3 = models.CharField(max_length=20,blank=True)
    code_4 = models.CharField(max_length=20,blank=True)

    line_of_business_1 = models.CharField(max_length=40, blank=True)
    line_of_business_2 = models.CharField(max_length=40,blank=True)
    line_of_business_3 = models.CharField(max_length=40,blank=True)
    line_of_business_4 = models.CharField(max_length=40,blank=True)

    receipts_1 = models.CharField(max_length=40, blank=True)
    receipts_2 = models.CharField(max_length=40,blank=True)
    receipts_3 = models.CharField(max_length=40,blank=True)
    receipts_4 = models.CharField(max_length=40,blank=True)

    subscribed_1 = models.CharField(max_length=40, blank=True)
    subscribed_2 = models.CharField(max_length=40,blank=True)
    subscribed_3 = models.CharField(max_length=40,blank=True)
    subscribed_4 = models.CharField(max_length=40,blank=True)

    paid_up_1 = models.CharField(max_length=40, blank=True)
    paid_up_2 = models.CharField(max_length=40,blank=True)
    paid_up_3 = models.CharField(max_length=40,blank=True)
    paid_up_4 = models.CharField(max_length=40,blank=True)

    employee_no_male_residing = models.PositiveIntegerField(default=0)
    employee_no_female_residing = models.PositiveIntegerField(default=0)
    
    delivery_trucks_no = models.PositiveIntegerField(verbose_name="Delivery Trucks/Vehicles No. of Units")
    estimated_area = models.CharField(verbose_name="Estimated area used in business", max_length=20, blank=True)

    owners_gender = models.PositiveSmallIntegerField(
        choices=Gender.choices,
        default=Gender.MALE
    )

    def __str__(self):
        return self.business_type