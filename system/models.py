from django.db import models
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

    business_name = models.CharField(blank=False, max_length=50, default='')
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
    community_tax_certificate = models.FileField(upload_to ='requirements/%Y/%m/%d/', blank=True)

    owners_gender = models.PositiveSmallIntegerField(
        choices=Gender.choices,
        default=Gender.MALE
    )

    def __str__(self):
        return self.business_type