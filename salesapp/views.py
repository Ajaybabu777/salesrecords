from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Salesrecord
from .forms import SalesrecordForm
import csv
from django.http import HttpResponse
from django.contrib import messages

def sales_record_list(request):
    query = request.GET.get('q')
    itemtype_search = request.GET.get('itemtype')
    region_filter = request.GET.get('region')
    country_filter = request.GET.get('country')
    sales_records = Salesrecord.objects.all()

    # Apply search query if exists
    if query:
        sales_records = sales_records.filter(
            Q(orderid__icontains=query) |
            Q(itemtype__icontains=query) |
            Q(region__icontains=query) |
            Q(country__icontains=query)
        )

    # Apply itemtype search if selected
    if itemtype_search:
        sales_records = sales_records.filter(itemtype__icontains=itemtype_search)

    # Apply region filter if selected
    if region_filter:
        sales_records = sales_records.filter(region=region_filter)

    # Apply country filter if selected
    if country_filter:
        sales_records = sales_records.filter(country=country_filter)

     # Get distinct regions and countries for filtering
    distinct_regions = Salesrecord.objects.values_list('region', flat=True).distinct()
    distinct_countries = Salesrecord.objects.values_list('country', flat=True).distinct()

    # Pagination
    paginator = Paginator(sales_records, 500)  # Show 500 records per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'sales_record_list.html', {
        'page_obj': page_obj,
        'distinct_regions': distinct_regions,
        'distinct_countries': distinct_countries,
    })


def edit_sales_record(request, pk):
    record = get_object_or_404(Salesrecord, pk=pk)
    
    if request.method == "POST":
        form = SalesrecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('sales_record_list')
    else:
        form = SalesrecordForm(instance=record)
    
    return render(request, 'edit_sales_record.html', {'form': form, 'record': record})


def add_sales_record(request):
    if request.method == "POST":
        form = SalesrecordForm(request.POST)
        if form.is_valid():
            sales_record = form.save(commit=False)
            sales_record.save()
            messages.success(request, 'Sales record added successfully!')
            return redirect('sales_record_list') 
            
    else:
        form = SalesrecordForm()
    
    return render(request, 'add_sales_record.html', {'form': form})

def download_sales_records(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sales_records.csv"'

    writer = csv.writer(response)
    writer.writerow(['Order ID', 'Region', 'Country', 'Item Type', 'Sales Channel', 'Order Priority', 
                     'Order Date', 'Ship Date', 'Units Sold', 'Unit Price', 'Unit Cost', 
                     'Total Revenue', 'Total Cost', 'Total Profit'])

    for record in Salesrecord.objects.all():
        writer.writerow([record.orderid, record.region, record.country, record.itemtype, record.saleschannel, 
                         record.orderpriority, record.orderdate, record.shipdate, record.unitssold, 
                         record.unitprice, record.unitcost, record.totalrevenue, 
                         record.totalcost, record.totalprofit])

    return response