from rest_framework import routers
from .views import AidTypeViewSet, AidBeneficiaryViewSet, DistributionRecordViewSet

router = routers.DefaultRouter()
router.register(r'aidtypes', AidTypeViewSet)
router.register(r'beneficiaries', AidBeneficiaryViewSet)
router.register(r'distributions', DistributionRecordViewSet)

urlpatterns = router.urls
