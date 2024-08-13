from django.db import models


class FinancialData(models.Model):
    company_name = models.CharField(max_length=255)  # New field for the company name
    net_profit_to_total_assets = models.FloatField(null=True, blank=True)
    total_liabilities_to_total_assets = models.FloatField(null=True, blank=True)
    working_capital_to_total_assets = models.FloatField(null=True, blank=True)
    current_assets_to_short_term_liabilities = models.FloatField(null=True, blank=True)
    retained_earnings_to_total_assets = models.FloatField(null=True, blank=True)
    sales_to_total_assets = models.FloatField(null=True, blank=True)
    equity_to_total_assets = models.FloatField(null=True, blank=True)
    current_liabilities_to_total_assets = models.FloatField(null=True, blank=True)
    book_value_of_equity_to_total_liabilities = models.FloatField(null=True, blank=True)
    gross_profit_to_sales = models.FloatField(null=True, blank=True)
    sales_to_inventory = models.FloatField(null=True, blank=True)
    target = models.BooleanField()

    class Meta:
        verbose_name = "Financial Data"
        verbose_name_plural = "Financial Data"

    def __str__(self):
        return f"{self.company_name} - Financial Data ID: {self.id}" 
