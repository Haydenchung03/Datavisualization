from django.shortcuts import render
from django.http import HttpResponse
from numpy import NaN
from .models import customerAquisition, netProfit, netProfitMargin
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(response):
    return render(response, "DataAnalytics/home.html", {})

def login(request):
    

    return render(request, "DataAnalytics/login.html")

def Calculations(request):
    # gets net income
    calculations = {}
    if request.method == 'POST':
        
        profit = request.POST.get('profit')
        sales = request.POST.get('sales')
        try:
            # saves inputs in database and converts inputs to floats
            save1 = netProfitMargin()

            profit = float(profit)
            sales = float(sales)
            save1.profit = profit
            save1.sales = sales;
            netProfitMarginCalculation = (profit / sales) * 100
            save1.profitMargin1 = netProfitMarginCalculation
            save1.save()

            # profit = 100000 sales = 1000000 | sales / profit * 100 = margin of 10%
            
            
            calculations["Profit: "] = float(str((round(profit, 2))))
            calculations["Sales: "] = float(str((round(sales, 2))))
            calculations["Net Margin: "] = float(str((round(netProfitMarginCalculation, 2))))
            return render(request, "DataAnalytics/calculations.html", {'calculations': calculations})
        except ValueError:
            calculations["Error"] = "";
            return render(request, "DataAnalytics/calculations.html", {'calculations': calculations})
        
    else:
        return render(request, "DataAnalytics/calculations.html")

def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')
        name = request.POST.get('name')
        recipient_list = email;
        subject1 = "Name: " + name + "\nSubject: " + subject + "\nMessage: "+ message
        send_mail(email, subject1, recipient_list, [settings.EMAIL_HOST_USER], fail_silently=True)
        return render(request, "DataAnalytics/confirmation.html", {'email': email})
    return render(request, "DataAnalytics/contact.html", {})

