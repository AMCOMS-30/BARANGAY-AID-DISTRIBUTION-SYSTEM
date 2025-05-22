from rest_framework import serializers
from .models import AidType, AidBeneficiary, DistributionRecord, AidApplication

class AidTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AidType
        fields = '__all__'

class AidBeneficiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = AidBeneficiary
        fields = '__all__'

class DistributionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = DistributionRecord
        fields = '__all__'

class AidApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AidApplication
        fields = '__all__'
