from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import DateWidget

from GanesanTeam.models import Login, ClaimType, ClaimsTracker, Department, Divisions, Currency, Vendors_Brands, \
    Category, Serilized_NonSerilized, Forwarder_Code, ClaimsStatus, AdditionalClaimsStatus, Status, Regions

class loginresource(resources.ModelResource):
    class Meta:
        model=Login
        exclude = ('id',)
        import_id_fields = ('username',)

class loginadmin(ImportExportModelAdmin):
    resource_class = loginresource
    search_fields = ['username']
    list_display = ['username', 'password']

class CustomDateWidget(DateWidget):
    def render(self, value, obj=None):
        if value is None:
            return ''
        return value.strftime('%d-%m-%Y')


class claimtrackerresource(resources.ModelResource):

    ClaimedDate = fields.Field(column_name='ClaimedDate ', attribute='ClaimedDate', widget=CustomDateWidget(format='%d-%m-%Y'))
    ECI_Date = fields.Field(column_name='ECI_Date', attribute='ECI_Date', widget=CustomDateWidget(format='%d-%m-%Y'))
    DueDate_ExpiryDate = fields.Field(column_name='DueDate_ExpiryDate', attribute='DueDate_ExpiryDate', widget=CustomDateWidget(format='%d-%m-%Y'))
    ASP_FDR_Date = fields.Field(column_name='ASP_FDR_Date', attribute='ASP_FDR_Date', widget=CustomDateWidget(format='%d-%m-%Y'))
    RR_Date = fields.Field(column_name='RR_Date', attribute='RR_Date', widget=CustomDateWidget(format='%d-%m-%Y'))
    Unit_Collection_Date = fields.Field(column_name='Unit_Collection_Date', attribute='Unit_Collection_Date', widget=CustomDateWidget(format='%d-%m-%Y'))
    RPO_Date = fields.Field(column_name='RPO_Date', attribute='RPO_Date', widget=CustomDateWidget(format='%d-%m-%Y'))
    GRN_Date = fields.Field(column_name='GRN_Date', attribute='GRN_Date', widget=CustomDateWidget(format='%d-%m-%Y'))
    CN_Date  = fields.Field(column_name='CN_Date', attribute='CN_Date', widget=CustomDateWidget(format='%d-%m-%Y'))
    class Meta:
        model = ClaimsTracker

        fields = ('id',
        'Department', 'Divisions', 'ClaimType', 'Regions', 'RequestFrom',
        'Originator', 'ClaimedDate', 'ClaimRefNumber', 'Ponumber', 'cbn',
        'hporder', 'customer_request_date', 'Partner_Customername',
        'CustomerCode', 'Partner_location', 'CustomerReference',
        'RedingtonInvoice', 'Redington_Invoice_Date', 'SellUnitPrice',
        'TotalSellPrice', 'Currency', 'Customer_prf_Number', 'Vendors_Brands',
        'Category', 'Partnumber', 'Qty', 'PackId', 'BoxId', 'Serilized_NonSerilized',
        'SerialNumber', 'UnitPrice', 'TotalAmount', 'VendorInvNo', 'ECI_Date',
        'DueDate_ExpiryDate', 'ASP_FDR_Date', 'Call_Id', 'Detailed_Issue_Product',
        'PRF_Num', 'RR_Num', 'RR_Date', 'Unit_Collection_Date', 'CM_Num',
        'CM_Amount', 'RPO_Num', 'RPO_Date', 'GRN_Date', 'DHL_AWB_Num',
        'Forwarder_Code', 'Claims_Status', 'AdditionalClaimsstatus', 'Remarks',
        'Status', 'CN_No', 'CN_Date', 'CN_Value', 'CA', 'Ageingdays'
    )

        export_order = fields


class claimtrackeradmin(ImportExportModelAdmin):
    resource_class = claimtrackerresource
    list_display = ('id',
        'Department', 'Divisions', 'ClaimType', 'Regions', 'RequestFrom',
        'Originator', 'ClaimedDate', 'ClaimRefNumber', 'Ponumber', 'cbn',
        'hporder', 'customer_request_date', 'Partner_Customername',
        'CustomerCode', 'Partner_location', 'CustomerReference',
        'RedingtonInvoice', 'Redington_Invoice_Date', 'SellUnitPrice',
        'TotalSellPrice', 'Currency', 'Customer_prf_Number', 'Vendors_Brands',
        'Category', 'Partnumber', 'Qty', 'PackId', 'BoxId', 'Serilized_NonSerilized',
        'SerialNumber', 'UnitPrice', 'TotalAmount', 'VendorInvNo', 'ECI_Date',
        'DueDate_ExpiryDate', 'ASP_FDR_Date', 'Call_Id', 'Detailed_Issue_Product',
        'PRF_Num', 'RR_Num', 'RR_Date', 'Unit_Collection_Date', 'CM_Num',
        'CM_Amount', 'RPO_Num', 'RPO_Date', 'GRN_Date', 'DHL_AWB_Num',
        'Forwarder_Code', 'Claims_Status', 'AdditionalClaimsstatus', 'Remarks',
        'Status', 'CN_No', 'CN_Date', 'CN_Value', 'CA', 'Ageingdays'
    )
    list_filter = ('Department', 'Divisions', 'ClaimType', 'Regions', 'Status')
    search_fields = ('ClaimRefNumber', 'CustomerCode', 'Partner_Customername')



class Departmentresource(resources.ModelResource):
    class Meta:
        model=Department
class Departmentadmin(ImportExportModelAdmin):
    resource_class = Departmentresource


class Divisonsresource(resources.ModelResource):
    class Meta:
        model=Divisions
class Divisonadmin(ImportExportModelAdmin):
    resource_class = Divisonsresource


class ClaimTyperesource(resources.ModelResource):
    class Meta:
        model=ClaimType
class ClaimTypeadmin(ImportExportModelAdmin):
    resource_class =ClaimTyperesource



class Regionsresource(resources.ModelResource):
    class Meta:
        model=Regions
class Regionsadmin(ImportExportModelAdmin):
    resource_class = Regionsresource



class  Currencyresource(resources.ModelResource):
    class Meta:
        model= Currency
class  Currencyadmin(ImportExportModelAdmin):
    resource_class = Currencyresource


class Vendors_Brandsresource(resources.ModelResource):
    class Meta:
        model=Vendors_Brands
class Vendors_Brandsadmin(ImportExportModelAdmin):
    resource_class = Vendors_Brandsresource



class Categoryresource(resources.ModelResource):
    class Meta:
        model=Category
class Categoryadmin(ImportExportModelAdmin):
    resource_class = Categoryresource


class Serilized_NonSerilizedresource(resources.ModelResource):
    class Meta:
        model=Serilized_NonSerilized

class Serilized_NonSerilizedadmin(ImportExportModelAdmin):
    resource_class = Serilized_NonSerilizedresource


class Forwarder_Coderesource(resources.ModelResource):
    class Meta:
        model=Forwarder_Code
class Forwarder_Codeadmin(ImportExportModelAdmin):
    resource_class = Forwarder_Coderesource


class ClaimsStatusresource(resources.ModelResource):
    class Meta:
        model=ClaimsStatus
class ClaimsStatusadmin(ImportExportModelAdmin):
    resource_class = ClaimsStatusresource



class AdditionalClaimsStatusresource(resources.ModelResource):
    class Meta:
        model=AdditionalClaimsStatus
class AdditionalClaimsStatusadmin(ImportExportModelAdmin):
    resource_class = AdditionalClaimsStatusresource


class Statusresource(resources.ModelResource):
    class Meta:
        model=Status
class Statusadmin(ImportExportModelAdmin):
    resource_class = Statusresource




admin.site.site_header = 'Redserv'
admin.site.register(Login,loginadmin)
admin.site.register(Department,Departmentadmin)
admin.site.register(Divisions,Divisonadmin)
admin.site.register(ClaimType, ClaimTypeadmin)
admin.site.register(Regions,Regionsadmin)
admin.site.register(Currency,Currencyadmin)
admin.site.register(Serilized_NonSerilized,Serilized_NonSerilizedadmin)
admin.site.register(Vendors_Brands,Vendors_Brandsadmin)
admin.site.register(Category,Categoryadmin)
admin.site.register(ClaimsTracker,claimtrackeradmin)
admin.site.register(Forwarder_Code,Forwarder_Codeadmin)
admin.site.register(ClaimsStatus,ClaimsStatusadmin)
admin.site.register(AdditionalClaimsStatus,AdditionalClaimsStatusadmin)
admin.site.register(Status,Statusadmin)





