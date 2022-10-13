from django.db import models

# Create your models here.

# Model for net profit
# charField(max_length = 200)
class netProfit(models.Model):

    # Example net income
    netIncome = models.FloatField()
    revenue = models.FloatField()
    
    def __float__(self):
        # Sample return
        return (self.netIncome / self.revenue) * 100

class customerAquisition(models.Model):

    #Example customer aquisition
    marketing = models.FloatField()
    newCustomer = models.IntegerField()

    def __float__(self):
        # return cost of customer aquisition
        return (self.marketing / self.newCustomer)

class netProfitMargin(models.Model):
    profit = models.FloatField()
    sales = models.FloatField()
    
    profitMargin1 = models.FloatField()
    @property
    def profitMargin(self):
        if(self.profit != None and self.sales != None):
            profitMargin1 = (self.profit / self.sales) * 100
            return profitMargin1
