# Get user input and calculate tax
base_income: float = float(input('Enter your yearly income: '))
tax_rate: float = float(input('Enter your tax rate percentage: ')) / 100
taxed: float = base_income * tax_rate

# Display the data
print('=' * 40)
print('Income Tax Calculator')
print('=' * 40)
print(f'Base Income:              ${base_income:,.2f}')
print(f'Tax Rate:                 {tax_rate:.0%}')
print('-' * 40)
print(f'Yearly Tax (Base):        ${taxed:,.2f}')
print('=' * 40)

# Homework:
# 1. Add projections for how much tax you'd pay if you
# doubled and tripled your income.

print(f'Double Base Income:       ${2 * base_income:,.2f}')
print(f'Yearly Tax (Base):        ${2 * taxed:,.2f}')
print('=' * 40)
print(f'Triple Base Income:       ${3 * base_income:,.2f}')
print(f'Yearly Tax (Base):        ${3 * taxed:,.2f}')