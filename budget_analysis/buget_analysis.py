import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

budget = pd.read_csv("budget.csv", sep = ";")
# print(budget)
print(f'The data set contains a private budget, with {budget.shape[0]} rows and {budget.shape[1]} columns.')
print('The first difference noticed with this .csv file is that it used ";" as seperator not the standard ",".')

"""Aufgabe 2: Gesamtsumme für Einnahmen und Ausgaben berechnen"""

income = budget['In'].sum()
expenses = budget['Out'].sum()

b_start_date = budget["Date"].min()
sdate_form = datetime.strptime(b_start_date, "%Y-%m-%d").strftime("%d-%m-%Y")

b_end_date = budget["Date"].max()
edate_form = datetime.strptime(b_end_date, "%Y-%m-%d").strftime("%d-%m-%Y")

print(f'Total income for Mario and Laura between {sdate_form} and {edate_form} is {income:.2f}€.')
print(f'Total expenses for Mario and Laura between {sdate_form} and {edate_form} is {expenses:.2f}€.')
print(f'Total savings over the period {sdate_form} : {edate_form} is a total of {income - expenses:.2f}€.\n')

"""Aufgabe 3: Ausgaben pro Kategorie"""

cat_sum = budget.groupby(['Category']).sum()  

# print(cat_sum)
lar_exp_cat = cat_sum['Out'].idxmax()
lar_exp_tot = max(cat_sum["Out"])
lar_exp = 0.0
for i, v in enumerate(budget["Category"]):
    if lar_exp_cat == v:
        lar_exp = budget['Out'][i]
print(f'Their largest expense is "{lar_exp_cat}" with an individual payment amount of {lar_exp}€ and total payment amount of {lar_exp_tot}€ over the budget period.\n')

"""Aufgabe 4: Visualisiere die Ausgaben pro Kategorie"""

cat_sum_exp = cat_sum.drop(index='Income')
print(cat_sum_exp)

# sns_cat_sum = sns.barplot(data=cat_sum_exp, x = "Out", )
# sns_cat_sum.set_title("Expenses Per Category")
# sns_cat_sum.set_xlabel("Amount in €")
# sns_cat_sum.set_ylabel("Expense Categories")
# sns_cat_sum.get_figure().savefig("expenses_per_category.png", bbox_inches='tight')
# sns_cat_sum.figure.clf

"""Bonusaufgabe: Ausgaben pro Monat"""

budget['Date'] = pd.to_datetime(budget['Date'])
new_dfs = []
# for month, group in budget.groupby(pd.Grouper(key = 'Date', freq = 'M')):
#     new_df = pd.DataFrame(group)
#     var_name = f"{month.strftime('%B_%Y')}"
#     #print(new_df['In'].sum())
#     print(f"The budget for {var_name} had {new_df['In'].sum():.2f}€ income with {new_df['Out'].sum():.2f}€ expenses leaving {new_df['In'].sum() - new_df['Out'].sum():.2f}€ savings.")
#     exec(f"{var_name} = new_df")
#     new_dfs.append(var_name)
#     #print(f"New var df '{var_name}'")
#     #print(new_df.head())
#     new_df_d = new_df[new_df['Category'] != 'Income']
#     sns_new_df = sns.barplot(data = new_df_d, x = "Category", y = "Out", ci = None)
#     sns_new_df.set_title(f"Expenses Per Category For {var_name}")
#     sns_new_df.set_xlabel(f"{var_name}")
#     sns_new_df.set_ylabel("Expense Amount €")
#     plt.xticks(rotation = 45, ha = 'right')
#     sns_new_df.get_figure().savefig(f'cost_per_{var_name}', bbox_inches = 'tight')
    # sns_new_df.figure.clf

# print(f'List of new dfs:{new_dfs}\n')        
# for i, v in enumerate(new_dfs):
#     df = globals()[v]
#     print(f'This is {v}:\n {df.head()}\n')

sum_monthly = budget[['Date', 'Out']].groupby(pd.Grouper(key = 'Date', freq = 'M')).sum()
sns_mnt_plot = sns.barplot(data = sum_monthly, x = sum_monthly.index.month_name(), y = "Out", errorbar=None)
sns_mnt_plot.set_title(f"Expenses Per Month")
sns_mnt_plot.set_xlabel(f"Months")
sns_mnt_plot.set_ylabel("Expense Amount €")
plt.xticks(rotation = 45, ha = 'right')
sns_mnt_plot.get_figure().savefig(f'cost_per_month', bbox_inches = 'tight')
sns_mnt_plot.figure.clf()
