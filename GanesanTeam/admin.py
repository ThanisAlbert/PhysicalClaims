from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import DateWidget

from GanesanTeam.models import Login, ClaimType, Region, Category, SubCategory, Claimsstatus, AdditionalClaimsstatus, \
    Originator, RequestFrom
from GanesanTeam.models import Tracker

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
    eci_date = fields.Field(column_name='eci_date', attribute='eci_date', widget=CustomDateWidget(format='%d-%m-%Y'))
    call_iddate = fields.Field(column_name='call_iddate', attribute='call_iddate', widget=CustomDateWidget(format='%d-%m-%Y'))
    rpo_date = fields.Field(column_name='rpo_date', attribute='rpo_date', widget=CustomDateWidget(format='%d-%m-%Y'))
    grn_date = fields.Field(column_name='grn_date', attribute='grn_date', widget=CustomDateWidget(format='%d-%m-%Y'))
    hpcn_date = fields.Field(column_name='hpcn_date', attribute='hpcn_date', widget=CustomDateWidget(format='%d-%m-%Y'))
    req_date = fields.Field(column_name='req_date', attribute='req_date', widget=CustomDateWidget(format='%d-%m-%Y'))
    current_date = fields.Field(column_name='current_date', attribute='current_date', widget=CustomDateWidget(format='%d-%m-%Y'))
    claim_date = fields.Field(column_name='claim_date', attribute='claim_date', widget=CustomDateWidget(format='%d-%m-%Y'))

    class Meta:
        model = Tracker
        # List all fields you want to export
        fields = ('id','claimtype', 'claim_ref', 'request_from', 'req_date', 'current_date', 'region',
                  'category', 'subcategory', 'claim_date', 'customer', 'purchase_order', 'cbn',
                  'hporder', 'recieved_partno', 'claimed_partno', 'qty', 'packid', 'boxid', 'serialno',
                  'unitprice', 'totalamount', 'hpinvno', 'redington_invoice', 'eci_date', 'call_iddate',
                  'rr', 'customercm_callid', 'dhlawb_forwardercode', 'rpo', 'rpo_date', 'grn_date',
                  'hpcn_no', 'hpcn_date', 'hpcn_value', 'ca', 'aging_days', 'claims_status',
                  'additional_claimsstatus', 'originator', 'remarks')

        export_order = fields



class claimtrackeradmin(ImportExportModelAdmin):
    resource_class = claimtrackerresource
    list_display = ['id','claimtype','claim_ref','request_from','req_date','current_date','region','category','subcategory','claim_date','customer','purchase_order','cbn','hporder','recieved_partno','claimed_partno','qty','packid','boxid','serialno','unitprice','totalamount','hpinvno','redington_invoice','eci_date','call_iddate','rr','customercm_callid','dhlawb_forwardercode','rpo','rpo_date','grn_date','hpcn_no','hpcn_date','hpcn_value','ca','aging_days','claims_status','additional_claimsstatus','originator','remarks']


class claimtyperesource(resources.ModelResource):
    class Meta:
        model=ClaimType

class claimtypeadmin(ImportExportModelAdmin):
    resource_class = claimtyperesource


class requestfromresource(resources.ModelResource):
    class Meta:
        model=RequestFrom

class requestfromadmin(ImportExportModelAdmin):
    resource_class = requestfromresource


class regionfromresource(resources.ModelResource):
    class Meta:
        model=Region
class regionfromadmin(ImportExportModelAdmin):
    resource_class = regionfromresource


class categoryresource(resources.ModelResource):
    class Meta:
        model=Category
class categoryadmin(ImportExportModelAdmin):
    resource_class = categoryresource


class subcategoryresource(resources.ModelResource):
    class Meta:
        model=SubCategory
class subcategoryadmin(ImportExportModelAdmin):
    resource_class = subcategoryresource


class claimstatusresource(resources.ModelResource):
    class Meta:
        model=Claimsstatus
class claimstatusadmin(ImportExportModelAdmin):
    resource_class = claimstatusresource


class additionalclaimstatusresource(resources.ModelResource):
    class Meta:
        model=AdditionalClaimsstatus
class additionalclaimstatusadmin(ImportExportModelAdmin):
    resource_class = additionalclaimstatusresource



class originatorresource(resources.ModelResource):
    class Meta:
        model=Originator
class originatoradmin(ImportExportModelAdmin):
    resource_class = originatorresource


admin.site.site_header = 'Redserv'
admin.site.register(Login,loginadmin)
admin.site.register(Tracker,claimtrackeradmin)
admin.site.register(ClaimType,claimtypeadmin)
admin.site.register(RequestFrom,requestfromadmin)
admin.site.register(Region,regionfromadmin)
admin.site.register(Category,categoryadmin)
admin.site.register(SubCategory,subcategoryadmin)
admin.site.register(Claimsstatus,claimstatusadmin)
admin.site.register(AdditionalClaimsstatus,additionalclaimstatusadmin)
admin.site.register(Originator,originatoradmin)




