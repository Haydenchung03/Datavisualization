from django.shortcuts import render
from django.http import HttpResponse
from .models import customerAquisition, netProfit
# Create your views here.

def home(response):
    return render(response, "DataAnalytics/home.html", {})


def netIncome(response, id):
    # gets net income
    ls = netProfit.objects.get(id = id)
    
    ls1 = (ls.netIncome / ls.revenue) * 100
    
    return render(response, "DataAnalytics/Calculations.html", {"ls1": ls1 })

def customer(response, id):
    # get customer squisition cost
    ls = customerAquisition.objects.get(id = id)
    ls1 = (ls.marketing / ls.newCustomer)
    return render(response, "DataAnalytics/Calculations.html", {"ls1": ls1 })

