from django.shortcuts import redirect, render

from .models import FinancialData
from .forms import CompanyFinancialsForm, FinancialDataForm
import joblib
from joblib import load
import pickle
import os



model_path = os.path.join('savedModels', 'V1_Ensemble_stacking_model_under.pkl')
try:
    with open(model_path, 'rb') as file:
        model = joblib.load(model_path)    
        print("Model loaded successfully.")
except FileNotFoundError:
    print(f"Error: The file {model_path} was not found.")
except pickle.UnpicklingError:
    print(f"Error: The file {model_path} could not be unpickled.")
except Exception as e:
    print(f"An error occurred while loading the model: {e}")


def homePage(request):
    return render(request,'home.html')

def table(request):
    financial_data_entries = FinancialData.objects.all()
    form = CompanyFinancialsForm()
    if request.method == 'POST':
        form = CompanyFinancialsForm(request.POST)
        if form.is_valid():
            net_profit = form.cleaned_data['net_profit']
            total_assets = form.cleaned_data['total_assets']
            total_liabilities = form.cleaned_data['total_liabilities']
            working_capital = form.cleaned_data['working_capital']
            current_assets = form.cleaned_data['current_assets']
            short_term_liabilities = form.cleaned_data['short_term_liabilities']
            retained_earnings = form.cleaned_data['retained_earnings']
            sales = form.cleaned_data['sales']
            equity = form.cleaned_data['equity']
            current_liabilities = form.cleaned_data['current_liabilities']
            book_value_of_equity = form.cleaned_data['book_value_of_equity']
            gross_profit = form.cleaned_data['gross_profit']
            inventory = form.cleaned_data['inventory']            

            net_profit_to_total_assets = net_profit / total_assets if total_assets else 0
            total_liabilities_to_total_assets = total_liabilities / total_assets if total_assets else 0
            working_capital_to_total_assets = working_capital / total_assets if total_assets else 0
            current_assets_to_short_term_liabilities = current_assets / short_term_liabilities if short_term_liabilities else 0
            retained_earnings_to_total_assets = retained_earnings / total_assets if total_assets else 0
            sales_to_total_assets = sales / total_assets if total_assets else 0
            equity_to_total_assets = equity / total_assets if total_assets else 0
            current_liabilities_to_total_assets = current_liabilities / total_assets if total_assets else 0
            book_value_of_equity_to_total_liabilities = book_value_of_equity / total_liabilities if total_liabilities else 0
            gross_profit_to_sales = gross_profit / sales if sales else 0
            sales_to_inventory = sales / inventory if inventory else 0           

            features = [
                net_profit_to_total_assets,
                total_liabilities_to_total_assets,
                working_capital_to_total_assets,
                current_assets_to_short_term_liabilities,
                retained_earnings_to_total_assets,
                sales_to_total_assets,
                equity_to_total_assets,
                current_liabilities_to_total_assets,
                book_value_of_equity_to_total_liabilities,
                gross_profit_to_sales,
                sales_to_inventory
            ]
            
            features = [features]  
            
            target = model.predict(features)
            target = target[0]
            
            if target == 0:
                prediction = "NOT BANKRUPT"
            elif target == 1:
                prediction = "BANKRUPT"

            print("-------------------------------", prediction)
            financial_data_form = FinancialDataForm({
                'company_name': form.cleaned_data['name_of_company'],
                'net_profit_to_total_assets': net_profit_to_total_assets,
                'total_liabilities_to_total_assets': total_liabilities_to_total_assets,
                'working_capital_to_total_assets': working_capital_to_total_assets,
                'current_assets_to_short_term_liabilities': current_assets_to_short_term_liabilities,
                'retained_earnings_to_total_assets': retained_earnings_to_total_assets,
                'sales_to_total_assets': sales_to_total_assets,
                'equity_to_total_assets': equity_to_total_assets,
                'current_liabilities_to_total_assets': current_liabilities_to_total_assets,
                'book_value_of_equity_to_total_liabilities': book_value_of_equity_to_total_liabilities,
                'gross_profit_to_sales': gross_profit_to_sales,
                'sales_to_inventory': sales_to_inventory,
                'target': target
            })
            
            if financial_data_form.is_valid():
                financial_data_form.save()
                return redirect('table')
   
    return render(request,'table.html', {'form': form,'financial_data_entries': financial_data_entries})

def ourModel(request):
    return render(request,'OurModel.html')

def about(request):
    return render(request,'About.html')

