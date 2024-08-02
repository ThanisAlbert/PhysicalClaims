from django.db import models

# Create your models here.
class Login(models.Model):

    username = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = "Login"




class Department(models.Model):
    Department = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Department
    class Meta:
        verbose_name_plural = "Department"


class Divisions(models.Model):
    Divisions = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Divisions
    class Meta:
        verbose_name_plural = "Divisons"


class ClaimType(models.Model):
    claimtype = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.claimtype
    class Meta:
        verbose_name_plural = "ClaimsType"


class Regions(models.Model):
    Regions = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Regions
    class Meta:
        verbose_name_plural = "Regions"


class Currency(models.Model):
    Currency = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Currency
    class Meta:
        verbose_name_plural = "Currency"


class Vendors_Brands(models.Model):
    Vendors_Brands = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Vendors_Brands
    class Meta:
        verbose_name_plural = "Vendors_Brands"


class Category(models.Model):
    Category = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Category
    class Meta:
        verbose_name_plural = "Category"


class Serilized_NonSerilized(models.Model):
    Serilized_NonSerilized = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Serilized_NonSerilized
    class Meta:
        verbose_name_plural = "Serilized_NonSerilized"


class Forwarder_Code(models.Model):
    Forwarder_Code = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Forwarder_Code
    class Meta:
        verbose_name_plural = "Forwarder_Code"


class ClaimsStatus(models.Model):
    ClaimsStatus = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.ClaimsStatus
    class Meta:
        verbose_name_plural = "ClaimsStatus"


class AdditionalClaimsStatus(models.Model):
    AdditionalClaimsStatus = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.AdditionalClaimsStatus
    class Meta:
        verbose_name_plural = "AdditionalClaimsStatus"


class Status (models.Model):
    Status = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.Status
    class Meta:
        verbose_name_plural = "Status"


class ClaimsTracker(models.Model):
    id = models.CharField(primary_key=True,max_length=20)
    Department = models.CharField(max_length=100, null=True, blank=True)
    Divisions = models.CharField(max_length=100, null=True, blank=True)
    ClaimType = models.CharField(max_length=100, null=True, blank=True)
    Regions = models.CharField(max_length=100, null=True, blank=True)
    RequestFrom = models.CharField(max_length=100, null=True, blank=True)
    Originator = models.CharField(max_length=100, null=True, blank=True)
    ClaimedDate = models.DateTimeField(null=True, blank=True)
    ClaimRefNumber= models.CharField(max_length=100, null=True, blank=True)

    Ponumber = models.CharField(max_length=20, null=True, blank=True)
    cbn = models.CharField(max_length=100, null=True, blank=True)
    hporder = models.CharField(max_length=100, null=True, blank=True)
    customer_request_date = models.DateTimeField(null=True, blank=True)
    Partner_Customername =models.CharField(max_length=100, null=True, blank=True)

    CustomerCode=models.CharField(max_length=100, null=True, blank=True)
    Partner_location = models.CharField(max_length=100, null=True, blank=True)
    CustomerReference = models.CharField(max_length=100, null=True, blank=True)
    RedingtonInvoice = models.CharField(max_length=100, null=True, blank=True)
    Redington_Invoice_Date=models.DateTimeField(null=True,blank=True)
    SellUnitPrice = models.CharField(max_length=20, null=True, blank=True)
    TotalSellPrice = models.CharField(max_length=20, null=True, blank=True)
    Currency=models.CharField(max_length=20, null=True, blank=True)
    Customer_prf_Number = models.CharField(max_length=50, null=True, blank=True)
    Vendors_Brands = models.CharField(max_length=50, null=True, blank=True)

    Category = models.CharField(max_length=50, null=True, blank=True)
    Partnumber = models.CharField(max_length=50, null=True, blank=True)
    Qty = models.CharField(max_length=10, null=True, blank=True)
    PackId = models.CharField(max_length=50, null=True, blank=True)
    BoxId = models.CharField(max_length=50, null=True, blank=True)
    Serilized_NonSerilized = models.CharField(max_length=100, null=True, blank=True)
    SerialNumber = models.CharField(max_length=100, null=True, blank=True)

    UnitPrice = models.CharField(max_length=20, null=True, blank=True)
    TotalAmount = models.CharField(max_length=20, null=True, blank=True)
    VendorInvNo = models.CharField(max_length=50, null=True, blank=True)
    ECI_Date = models.DateTimeField(null=True,blank=True)
    DueDate_ExpiryDate = models.DateTimeField(null=True,blank=True)
    ASP_FDR_Date = models.DateTimeField(null=True,blank=True)
    Call_Id = models.CharField(max_length=50, null=True, blank=True)
    Detailed_Issue_Product = models.CharField(max_length=50, null=True, blank=True)
    PRF_Num = models.CharField(max_length=50, null=True, blank=True)
    RR_Num = models.CharField(max_length=50, null=True, blank=True)
    RR_Date = models.DateTimeField(null=True,blank=True)
    Unit_Collection_Date = models.DateTimeField(null=True,blank=True)
    CM_Num = models.CharField(max_length=50, null=True, blank=True)
    CM_Amount = models.CharField(max_length=20, null=True, blank=True)

    RPO_Num = models.CharField(max_length=50, null=True, blank=True)
    RPO_Date = models.DateTimeField(null=True,blank=True)
    GRN_Date = models.DateTimeField(null=True,blank=True)
    DHL_AWB_Num = models.CharField(max_length=50, null=True, blank=True)
    Forwarder_Code = models.CharField(max_length=50, null=True, blank=True)
    Claims_Status = models.CharField(max_length=50, null=True, blank=True)
    AdditionalClaimsstatus = models.CharField(max_length=50, null=True, blank=True)
    Remarks = models.CharField(max_length=100, null=True, blank=True)
    Status = models.CharField(max_length=25, null=True, blank=True)
    CN_No = models.CharField(max_length=100, null=True, blank=True)
    CN_Date = models.DateTimeField(null=True,blank=True)
    CN_Value = models.CharField(max_length=100, null=True, blank=True)
    CA = models.CharField(max_length=10, null=True, blank=True)
    Ageingdays= models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = "ClaimsTracker"











































