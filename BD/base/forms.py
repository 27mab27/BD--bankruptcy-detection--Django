from django import forms

class CompanyFinancialsForm(forms.Form):
    name_of_company = forms.CharField(max_length=255, label="Name of company")
    net_profit = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Net Profit")
    total_assets = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Total Assets")
    total_liabilities = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Total Liabilities")
    working_capital = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Working Capital")
    current_assets = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Current Assets")
    short_term_liabilities = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Short-term Liabilities")
    retained_earnings = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Retained Earnings")  # Added field
    sales = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Sales")
    equity = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Equity")
    current_liabilities = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Current Liabilities")
    book_value_of_equity = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Book Value of Equity")
    gross_profit = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Gross Profit")
    inventory = forms.DecimalField(max_digits=20, decimal_places=2, required=False, label="Inventory")

from django import forms
from .models import FinancialData

class FinancialDataForm(forms.ModelForm):
    class Meta:
        model = FinancialData
        fields = [
            'company_name',
            'net_profit_to_total_assets',
            'total_liabilities_to_total_assets',
            'working_capital_to_total_assets',
            'current_assets_to_short_term_liabilities',
            'retained_earnings_to_total_assets',
            'sales_to_total_assets',
            'equity_to_total_assets',
            'current_liabilities_to_total_assets',
            'book_value_of_equity_to_total_liabilities',
            'gross_profit_to_sales',
            'sales_to_inventory',
            'target'
        ]

