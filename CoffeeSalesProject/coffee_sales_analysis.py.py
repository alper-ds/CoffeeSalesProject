import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns   

df = pd.read_csv('CoffeeSalesProject/coffee_sales.csv')
"""
print(df.describe())
print(df['coffee_name'].value_counts())
print(df.isnull().sum())

"""
# CLEANING DATA

df['money'].fillna(df['money'].mean(), inplace=True)
df.dropna(subset=['coffee_name','hour_of_day'], inplace=True)


# DATA ANALYSIS

total_revenue = df["money"].sum()
print("total_revenue:", total_revenue)

coffee_sales = df['coffee_name'].value_counts()
plt.bar(coffee_sales.index, coffee_sales.values, color="brown")
plt.xlabel("Coffee Type")
plt.ylabel("Number of Sales")
plt.show()

hourly_sales = df.groupby('hour_of_day')['money'].sum()
hourly_sales.plot(kind="bar", color = "skyblue")
plt.xlabel("Hour")
plt.ylabel("Revenue")
plt.show()

weekday_sales = df.groupby(['Weekdaysort','Weekday'])['money'].sum()
weekday_sales = weekday_sales.sort_index(level=0)
weekday_sales.plot(kind="bar", color="green")
plt.title("Sales by Weekday")
plt.show()

month_sales = df.groupby(['Monthsort','Month_name'])['money'].sum()
month_sales = month_sales.sort_index(level=0)
month_sales.plot(kind='bar', color="orange")
plt.title("Sales by Month")
plt.show()

payment_counts = df['cash_type'].value_counts()
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', colors = ["lightblue", 'pink'] )
plt.show()