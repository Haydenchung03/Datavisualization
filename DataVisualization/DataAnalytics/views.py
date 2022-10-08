from django.shortcuts import render
from django.http import HttpResponse
from .models import customerAquisition, netProfit
from django.core.mail import send_mail
from django.conf import settings

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

def login(request):
    

    return render(request, "DataAnalytics/login.html")

def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        recipient_list = email;
        subject1 = "Subject: " + subject + "\nMessage: "+ message
        send_mail(email, subject1, recipient_list, [settings.EMAIL_HOST_USER], fail_silently=True)
        return render(request, "DataAnalytics/confirmation.html", {'email': email})
    return render(request, "DataAnalytics/contact.html", {})

