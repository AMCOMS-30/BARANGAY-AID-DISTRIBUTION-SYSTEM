from django.shortcuts import render, redirect, get_object_or_404
from .models import AidBeneficiary, DistributionRecord, AidType
from .forms import AidApplicationForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
@require_POST
def delete_distribution(request, distribution_id):
    distribution = get_object_or_404(DistributionRecord, pk=distribution_id)
    distribution.delete()
    return redirect('manage_aid_applications')

def delete_beneficiary(request, beneficiary_id):
    beneficiary = get_object_or_404(AidBeneficiary, id=beneficiary_id)
    
    if request.method == 'POST':
        beneficiary.delete()
        messages.success(request, 'Beneficiary deleted successfully.')
    
    return redirect('manage_aid_applications')

def aid_home(request):
    return render(request, 'aid_home.html')

def apply_for_aid(request):
    aid_types = AidType.objects.all()  

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        age = request.POST.get('age')
        aid_type_id = request.POST.get('aid_type')

        if name and address and age and aid_type_id:
            try:
                aid_type = AidType.objects.get(pk=aid_type_id)
                AidBeneficiary.objects.create(
                    name=name,
                    address=address,
                    age=age,
                    aid_type=aid_type
                )
                return redirect('aid_confirmation')
            except AidType.DoesNotExist:
                pass  

    return render(request, 'apply_for_aid.html', {'aid_types': aid_types})

def aid_confirmation(request):
    return render(request, 'aid_confirmation.html')

def manage_aid_applications(request):
    applications = AidBeneficiary.objects.all()
    distributions = DistributionRecord.objects.all()
    return render(request, 'manage_aid_applications.html', {
        'applications': applications,
        'distributions': distributions
    })

def distribute_aid(request, beneficiary_id):
    beneficiary = get_object_or_404(AidBeneficiary, pk=beneficiary_id)
    aid_types = AidType.objects.all()

    if request.method == 'POST':
        aid_type = get_object_or_404(AidType, pk=request.POST['aid_type'])
        quantity = int(request.POST['quantity'])
        distribution_date = request.POST['distribution_date']
        description = request.POST['description']

        distribution = DistributionRecord(
            beneficiary=beneficiary,
            aid_type=aid_type,
            quantity=quantity,
            distribution_date=distribution_date,
            description=description,
            
        )
        distribution.save()
        return redirect('distribution_confirmation')

    return render(request, 'distribute_aid.html', {
        'beneficiary': beneficiary,
        'aid_types': aid_types
    })

def distribution_confirmation(request):
    return render(request, 'distribution_confirmation.html')

def select_beneficiary(request):
    beneficiaries = AidBeneficiary.objects.all()
    return render(request, 'select_beneficiary.html', {'beneficiaries': beneficiaries})


from rest_framework import viewsets
from .models import AidType, AidBeneficiary, DistributionRecord
from .serializers import AidTypeSerializer, AidBeneficiarySerializer, DistributionRecordSerializer

class AidTypeViewSet(viewsets.ModelViewSet):
    queryset = AidType.objects.all()
    serializer_class = AidTypeSerializer

class AidBeneficiaryViewSet(viewsets.ModelViewSet):
    queryset = AidBeneficiary.objects.all()
    serializer_class = AidBeneficiarySerializer

class DistributionRecordViewSet(viewsets.ModelViewSet):
    queryset = DistributionRecord.objects.all()
    serializer_class = DistributionRecordSerializer