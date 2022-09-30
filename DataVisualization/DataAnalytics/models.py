from django.db import models

# Create your models here.

# Model for net profit
class netProfit(models.Model):

    # Example net income
    netIncome = models.FloatField()
    revenue = models.FloatField()
    netProfit = (netIncome / revenue) * 100
    
    def __str__(self):
        return self.netProfit

class Item(models.Model):
    netProfitItem = models.ForeignKey(netProfit, on_delete=models.CASCADE)
    text = models.CharField(max_length = 300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

