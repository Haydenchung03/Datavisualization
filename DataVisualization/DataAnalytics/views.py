from django.shortcuts import render
from django.http import HttpResponse
from .models import customerAquisition, netProfit
# Create your views here.

def home(response):
    return render(response, "DataAnalytics/home.html", {})


def netIncome(response, id):
    # gets net income
    netIncome_dict = {}
    ls = netProfit.objects.get(id = id)
    
    ls1 = (ls.netIncome / ls.revenue) * 100
    
    netIncome_dict["ls1"] = ls1
    return render(response, "DataAnalytics/Calculations.html", netIncome_dict)

def customer(response, id):
    # get customer squisition cost
    customer_dict = {}
    ls = customerAquisition.objects.get(id = id)
    ls1 = (ls.marketing / ls.newCustomer)
    customer_dict["ls1"] = ls1
    return render(response, "DataAnalytics/Calculations.html", customer_dict)

