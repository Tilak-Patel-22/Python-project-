import pandas as pd 
import matplotlib.pyplot as plt

#Open file in read mode.
df=pd.read_csv(r"C:\Users\ASUS\Downloads\New Microsoft Excel Worksheet 2.csv")

#To check whether the file is successfully opened or not.
print(df.head())
print(df.info())

#1st Step is to remove bad data.
new_df = df.dropna() #This will remove all the rows with missing values.
print(new_df.to_string()) #This will print the entire dataframe.
