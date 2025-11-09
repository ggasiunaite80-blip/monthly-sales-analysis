#pvz duomenys su pardavimais uz paskutini menesi

#numpy
import numpy as np
products_ids = np.array([101, 102, 103, 104, 105, 106, 107, 108, 109, 110])
prices = np.array([10.99, 20.99, 15.49, 25.49, 5.99, 12.99, 7.99, 30.99, 18.99, 9.99])
quantities = np.array([100, 50, 75, 30, 200, 120, 150, 20, 80, 110])
dates = np.array([
    "2023-07-01", "2023-07-02", "2023-07-03", "2023-07-04", "2023-07-05", "2023-07-06", "2023-07-07", "2023-07-08", "2023-07-09", "2023-07-10"
])
total_sales = prices * quantities
print(f"Total prices: {total_sales}")

total_uzdarbis = np.sum(total_sales)
print(f"total uzdarbis: {total_uzdarbis}$")

avarage_check = np.mean(total_sales)
print(f"Vidutinis cekis: {avarage_check: .2f}$") 

best_product_index = np.argmax(total_sales)
worst_product_index = np.argmin(total_sales)
print(f"Best product (ID: {products_ids[best_product_index]} sales amount: {total_sales[best_product_index]}")
print(f"Worst product (ID: {products_ids[worst_product_index]} sales amount: {total_sales[worst_product_index]}")
 
 #pandas
import pandas as pd
dates_pd = pd.to_datetime(dates) 
days_of_week = dates_pd.day_name() 
print(f"Sales per week: {days_of_week}")

sales_by_day = dict() 
for day, sale in zip(days_of_week, total_sales): 
    if day in sales_by_day:
        sales_by_day[day] += sale
    else:
        sales_by_day[day] = sale 
print(f"Sales per days: {sales_by_day}") 

#matplotlib, seaborn
import matplotlib.pyplot as plt 
import seaborn as sns

plt.figure(figsize=(10, 6)) 
sns.barplot(x = products_ids, y = total_sales, palette ='Blues_d') 
plt.xlabel("Produkto ID") 
plt.ylabel("Pardavimu suma ($)") 
plt.title("Pardavimai pagal produktus") 
plt.show() 

plt.figure(figsize=(10,6))
sns.barplot(x = sales_by_day.keys(), y = sales_by_day.values(), palette ='Greens_d')
plt.xlabel("Savaitės diena")
plt.ylabel("Pardavimų suma ($)")
plt.title("Pardavimai pagal savaitės dienas")
plt.show()