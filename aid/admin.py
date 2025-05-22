from django.contrib import admin
from .models import AidBeneficiary, AidType, DistributionRecord


admin.site.register(AidBeneficiary)
admin.site.register(AidType)
admin.site.register(DistributionRecord)