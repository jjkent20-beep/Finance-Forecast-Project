
# ---------------------------
# Finance Forecast Project
# Scenario: 
# 22-year-old Recent Finance Graduate
# Base Salary: $125,000/year
# Annual Bonus: $20,000
# Lives in New York City
#Income (monthly)
# ---------------------------

monthly_salary = 10416.67
monthly_bonus = 1666.67
monthly_investment_income = 50
monthly_side_hustle_income = 200

total_monthly_income = (
+ monthly_salary  
+ monthly_bonus  
+ monthly_investment_income 
+ monthly_side_hustle_income )
print("Total Monthly Income: $", round(total_monthly_income,2))

# ---------------------------
# Fixed Expenses (monthly)
# ---------------------------
phone_bill = 76
internet = 50
utilities = 200
rent = 3700
life_insurance = 100
subscription_services = 150

# ---------------------------
# Variable Expenses (monthly)
# ---------------------------

groceries = 400
dining_out = 200
entertainment = 300
shopping = 200
transportation = 150
travel = 132
healthcare_insurance = 400

total_monthly_expenses = (
phone_bill  
+ internet  
+ utilities  
+ rent  
+ life_insurance 
+ subscription_services 
+ groceries  
+ dining_out  
+ entertainment  
+ shopping 
+ transportation 
+ travel 
+ healthcare_insurance)
print("Total Monthly Expenses: $", round(total_monthly_expenses,2))

net_monthly_cash_flow = total_monthly_income - total_monthly_expenses
print("Net Monthly Cash Flow: $", round(net_monthly_cash_flow, 2))

annual_income = total_monthly_income * 12
print("Annual Income: $", round(annual_income, 2))
annual_expenses = total_monthly_expenses * 12
print("Annual Expenses: $", round(annual_expenses, 2))
annual_cash_flow = net_monthly_cash_flow * 12
print("Annual Cash Flow: $", round(annual_cash_flow, 2))

# ---------------------------
#Savings and Investments (monthly)
# ---------------------------
investment_contribution = 800
retirement_contribution = 1000
monthly_savings = 300
emergency_fund_contribution = 300

total_monthly_savings = (
    investment_contribution
+ retirement_contribution
+ monthly_savings
+ emergency_fund_contribution
)
print("Total Monthly Savings: $", round(total_monthly_savings, 2))
annual_savings = total_monthly_savings * 12
print("Annual Savings: $", round(annual_savings, 2))
savings_rate = (total_monthly_savings / total_monthly_income) * 100
print("Savings Rate", round(savings_rate, 2), "%")

# ---------------------------
# 12 Month Savings Forecast
# ---------------------------
projected_savings_1_year = total_monthly_savings * 12
print("Projected Savings After 1 Year: $", round(projected_savings_1_year, 2))

# ---------------------------
# Investment Growth (1 Year)
# ---------------------------
annual_return_rate = 0.08
investment_value_after_1_year = annual_savings * (1 +annual_return_rate)
print("Investment Value After 1 Year: $", round(investment_value_after_1_year, 2))

# ---------------------------
# 5 Year Investment Forecast
# ---------------------------
investment_balance = annual_savings
for year in range(1, 6): 
    investment_balance = investment_balance * (1+ annual_return_rate)
    print("Year", year, "Investment Balance: $", round(investment_balance, 2))

# ---------------------------
# Emergency Fund Goal
# ---------------------------
emergency_fund_goal = total_monthly_expenses * 6
print("Recommended Emergency Fund: $", round(emergency_fund_goal, 2))

# ---------------------------
# Net Worth Calculations
# ---------------------------
cash = 15000
investments = 50000
retirement_account = 25000
student_loans = 20000
credit_card_debt = 3000

# ---------------------------
# Net Worth Calculations
# ---------------------------
cash = 10000
investments = 15000 
retirement_account = 8000
student_loans = 25000
credit_card_debt = 1000
total_assets = (
    cash
    + investments
    + retirement_account
)
total_liabilities = (
    student_loans
    + credit_card_debt
)
net_worth = total_assets - total_liabilities
print("Total Assets: $", round(total_assets, 2))
print("Total Liabilities: $", round(total_liabilities, 2))
print("Net Worth: $", round(net_worth, 2))

# ---------------------------
# Salary Raise Scenario
# ---------------------------
raise_percentage = 0.10
new_annual_salary = 125000 * (1 + raise_percentage)
print("Salary After 10% Raise: $", round(new_annual_salary, 2))

new_monthly_salary = new_annual_salary / 12
print("Monthly Salary After 10% Raise: $", round(new_monthly_salary, 2))

new_total_monthly_income = (
    new_monthly_salary
    + monthly_bonus
    + monthly_investment_income
    + monthly_side_hustle_income
)
print("New Total Monthly Income After Raise: $", round(new_total_monthly_income, 2))
new_monthly_cash_flow = new_total_monthly_income - total_monthly_expenses
print("New Monthly Cash Flow After Raise: $", round(new_monthly_cash_flow, 2))

# ---------------------------
# Estimated Taxes
# ---------------------------
tax_rate = 0.25
estimated_annual_taxes = annual_income * tax_rate
after_tax_income = annual_income - estimated_annual_taxes
print("Estimated Annual Taxes: $", round(estimated_annual_taxes, 2))
print("After-Tax Annual Income: $", round(after_tax_income, 2))

after_tax_monthly_income = after_tax_income / 12
print("After-Tax Monthly Income: $", round(after_tax_monthly_income, 2))

debt_to_assets_ratio = (total_liabilities / total_assets) * 100
print("Debt-to-Asset Ratio", round(debt_to_assets_ratio, 2), "%")