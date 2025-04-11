import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#Load data
df = pd.read_csv(r"C:\Users\ASUS\Downloads\New Microsoft Excel Worksheet 2.csv")

#Preview
print("Initial Data:")
print(df.head())
print(df.info())

#Replace missing addresses with "not known"
df["CONSI_ADD1"] = df["CONSI_ADD1"].fillna("not known")
df["CONSI_ADD2"] = df["CONSI_ADD2"].fillna("not known")

#Drop unnecessary columns
df.drop(columns=["Driver Name", "Mobile Number"], inplace=True, errors='ignore')

#Save cleaned file
df.to_csv("cleaned_sales_data.csv", index=False)

#visualize missing data
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap="viridis") #heatmap use because to show patterns clearly.
                                                     #cbar = false means it tells Seaborn not to display the color bar.
plt.title("Missing Value Heatmap")
plt.show()

#Show cleaned data sample
print("Cleaned Data:") 
print(df.head(20))

# 1. Product-wise Sales Performance
plt.figure(figsize=(10,5))
product_sales = df.groupby('PRODUCT')['INV_AMT'].sum().sort_values(ascending=False).head(10) #ascending = False means it starts from highest value
product_sales.plot(kind='barh', title='Top 10 Product-wise Sales Performance')
plt.xlabel('Sales')
plt.tight_layout() #It is used to adjust everything without overlapping. 
plt.show()

# 2. Product Sales Insights and Trends
plt.figure(figsize=(10,5))
trend_data = df.groupby(['INV_DATE', 'PRODUCT'])['INV_AMT'].sum().fillna(0)
trend_data.plot(kind='line', title='Product Sales Trends Over Time')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# 3. Product Net Weight vs Sales Correlation
plt.figure(figsize=(6, 4))
sns.scatterplot(data=df, x='NET_WT', y='INV_AMT')
plt.title('Product Net Weight vs Sales')
plt.tight_layout()
plt.show()

# 4. City-wise Sales Analysis
plt.figure(figsize=(10,5))
city_sales = df.groupby('CONSI_CITY')['INV_AMT'].sum().sort_values(ascending=False).head(10)
city_sales.plot(kind='bar', title='Top 10 City-wise Sales')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
