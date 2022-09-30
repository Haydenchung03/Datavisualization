from django.db import models

# Create your models here.

# Model for net profit
class netProfit(models.Model):

    # Example net income
    netIncome = models.FloatField()
    revenue = models.FloatField()
    
    def __str__(self):
        return (self.netIncome / self.revenue) * 100

class Item(models.Model):
    netProfitItem = models.ForeignKey(netProfit, on_delete=models.CASCADE)
    text = models.CharField(max_length = 300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text

