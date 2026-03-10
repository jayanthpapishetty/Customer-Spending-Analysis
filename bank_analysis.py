import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("customer_transactions.xlsx")

print("Dataset Preview")
print(df.head())

# Total spending
total_spending = df["Amount"].sum()
print("\nTotal Spending:", total_spending)

# Spending by category
category_spending = df.groupby("Category")["Amount"].sum()
print("\nSpending by Category")
print(category_spending)

# Top customers
top_customers = df.groupby("CustomerID")["Amount"].sum().sort_values(ascending=False)
print("\nTop Customers")
print(top_customers)

# Visualization
category_spending.plot(kind="bar")
plt.title("Customer Spending by Category")
plt.xlabel("Category")
plt.ylabel("Total Amount")
plt.show()