from django.db import models

# Create your models here.

# Model for net profit
class netProfit(models.Model):

    # Example net income
    netIncome = models.FloatField()
    revenue = models.FloatField()
    
    
    def __float__(self):
        return (self.netIncome / self.revenue) * 100

