from django.shortcuts import render
from django.http import HttpResponse
from .models import customerAquisition, netProfit
# Create your views here.

def main(request, id):
    # gets net income
    ls = netProfit.objects.get(id = id)
    
    ls1 = (ls.netIncome / ls.revenue) * 100
    
    return HttpResponse("<h1>%s<h1>" %ls1)

def customer(request, id):
    # get customer squisition cost
    ls = customerAquisition.objects.get(id = id)
    ls1 = (ls.marketing / ls.newCustomer)
    return HttpResponse("<h1>%s<h1>" %ls1)

def v1(request):
    return HttpResponse("<h1>views 1<h1>")