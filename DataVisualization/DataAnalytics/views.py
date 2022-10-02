from django.shortcuts import render
from django.http import HttpResponse
from .models import customerAquisition, netProfit
# Create your views here.

def home(response):
    return render(response, "DataAnalytics/home.html", {})


def Calculations(response, id):
    # gets net income
    calculations = {}
    netCalculationGet = netProfit.objects.get(id = id)
    netCalculationFormula = (netCalculationGet.netIncome / netCalculationGet.revenue) * 100
    
    # Customer Aquisition costs
    customerAquisitionGet = customerAquisition.objects.get(id = id)
    customerFormula = (customerAquisitionGet.marketing / customerAquisitionGet.newCustomer)

    calculations["netCalculationGet"] = netCalculationGet.netIncome,  netCalculationGet.revenue
    calculations["netCalculationFormula"] = netCalculationFormula
    calculations["customerAquisitionGet"] = customerAquisitionGet.marketing, customerAquisitionGet.newCustomer
    calculations["customerFormula"] = customerFormula
    return render(response, "DataAnalytics/calculations.html", calculations)

def login(response):
    
    return render(response, "DataAnalytics/login.html")

def contact(response):
    return render(response, "DataAnalytics/contact.html")

