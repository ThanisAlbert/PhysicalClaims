from django.db import models

# Create your models here.
class Login(models.Model):

    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "Login"


class ClaimType(models.Model):
    claimtype = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.claimtype
    class Meta:
        verbose_name_plural = "ClaimsType"


class RequestFrom(models.Model):
    requestfrom = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.requestfrom
    class Meta:
        verbose_name_plural = "RequestFrom"


class Region(models.Model):
    region = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.region
    class Meta:
        verbose_name_plural = "Region"


class Category(models.Model):
    category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.category
    class Meta:
        verbose_name_plural = "Category"

class SubCategory(models.Model):
    subcategory = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.subcategory
    class Meta:
        verbose_name_plural = "SubCategory"

class Claimsstatus(models.Model):
    claimsstatus = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.claimsstatus
    class Meta:
        verbose_name_plural = "Claimsstatus"

class AdditionalClaimsstatus(models.Model):
    additionalclaimsstatus = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.additionalclaimsstatus
    class Meta:
        verbose_name_plural = "AdditionalClaimsstatus"


class Originator(models.Model):
    originator = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.originator
    class Meta:
        verbose_name_plural = "Originator"


class Tracker(models.Model):

    claimtype = models.CharField(max_length=100,null=True,blank=True)
    claim_ref = models.CharField(max_length=100,null=True,blank=True)
    request_from = models.CharField(max_length=100,null=True,blank=True)
    req_date = models.DateField(null=True, blank=True)
    current_date = models.DateField(null=True, blank=True)
    region = models.CharField(max_length=10,null=True,blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    subcategory = models.CharField(max_length=100, null=True, blank=True)
    claim_date = models.DateField(null=True, blank=True)
    customer = models.CharField(max_length=100, null=True, blank=True)
    purchase_order = models.CharField(max_length=100, null=True, blank=True)
    cbn = models.CharField(max_length=100, null=True, blank=True)
    hporder = models.CharField(max_length=100, null=True, blank=True)
    recieved_partno = models.CharField(max_length=100, null=True, blank=True)
    claimed_partno = models.CharField(max_length=100, null=True, blank=True)
    qty = models.CharField(max_length=100, null=True, blank=True)
    packid = models.CharField(max_length=100, null=True, blank=True)
    boxid = models.CharField(max_length=100, null=True, blank=True)
    serialno = models.CharField(max_length=100, null=True, blank=True)
    unitprice = models.CharField(max_length=50, null=True, blank=True)
    totalamount = models.CharField(max_length=50, null=True, blank=True)
    hpinvno = models.CharField(max_length=100,null=True,blank=True)
    redington_invoice = models.CharField(max_length=100,null=True,blank=True)
    eci_date = models.DateField(null=True, blank=True)
    call_iddate = models.DateField(null=True, blank=True)
    rr = models.CharField(max_length=100,null=True,blank=True)
    customercm_callid = models.CharField(max_length=100,null=True,blank=True)
    dhlawb_forwardercode = models.CharField(max_length=100,null=True,blank=True)
    rpo = models.CharField(max_length=100,null=True,blank=True)
    rpo_date = models.DateField(null=True, blank=True)
    grn_date = models.DateField(null=True, blank=True)
    hpcn_no = models.CharField(max_length=100,null=True,blank=True)
    hpcn_date = models.DateField(null=True, blank=True)
    hpcn_value = models.CharField(max_length=100,null=True,blank=True)
    ca = models.CharField(max_length=100,null=True,blank=True)
    aging_days = models.CharField(max_length=100,null=True,blank=True)
    claims_status = models.CharField(max_length=100,null=True,blank=True)
    additional_claimsstatus =  models.CharField(max_length=100,null=True,blank=True)
    originator = models.CharField(max_length=100,null=True,blank=True)
    remarks = models.CharField(max_length=100,null=True,blank=True)

    class Meta:
        verbose_name_plural = "ClaimsTracker"












