from django.db import models

class AidType(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=10, null=True)
    def __str__(self):
        return self.name

class AidBeneficiary(models.Model):
     name = models.CharField(max_length=100)
     address = models.CharField(max_length=200)
     age = models.IntegerField()
     aid_type = models.ForeignKey(AidType, on_delete=models.CASCADE)
     status = models.CharField(choices= [('approved', 'Approved'), ('denied', 'Denied')], max_length=10, default='denied')
     date_received = models.DateField(null=True, blank=True)

     def __str__(self):
        return self.name

class DistributionRecord(models.Model):
    beneficiary = models.ForeignKey(AidBeneficiary, on_delete=models.CASCADE)
    aid_type = models.ForeignKey(AidType, on_delete=models.CASCADE)            
    quantity = models.IntegerField()
    distribution_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.beneficiary.name} - {self.aid_type.name} -  {self.distribution_date}"


class AidApplication(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    age = models.IntegerField()
    aid_type = models.ForeignKey(AidType, on_delete=models.CASCADE)
