from django.contrib import admin

from salesapp.models import Salesrecord

# Register your models here.

class SalesrecordAdmin(admin.ModelAdmin):
    list_display = (
        'orderid', 'itemtype', 'orderdate', 'unitssold', 
        'unitprice', 'unitcost', 'totalrevenue', 'totalcost', 'totalprofit'
    )
    search_fields = ('orderid', 'itemtype', 'region', 'country')
    list_filter = ('region', 'country', 'saleschannel', 'orderpriority')
    readonly_fields = ('totalrevenue', 'totalcost', 'totalprofit')

admin.site.register(Salesrecord, SalesrecordAdmin)