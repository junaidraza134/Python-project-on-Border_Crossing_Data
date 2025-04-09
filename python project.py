import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

dic=pd.read_csv("C:\\Users\\junai\\OneDrive\\Desktop\\Border_Crossing_Entry_Data.csv")
df=pd.DataFrame(dic)
#print(df)

infromation=df.info()
#print(information)

describe=df.describe()
#print(describe)

h_ead=df.head()
#print(h_ead)

t_ail=df.tail()
#print(t_ail)

drop_na=df.dropna()
#print(drop_na)

is_null_sum=df.isnull().sum()
#print(is_null_sum)

is_null_sum_sum=df.isnull().sum().sum()
#print(is_null_sum_sum)

is_null=df.isnull()
#print(is_null)

unique_value=df['Border'].unique()
#print(unique_value)

us_border_df = df[df['Border'] == 'US-Mexico Border']
#print(us_border_df.head())

df_filled = df.fillna("Unknown")
#print(df_filled)

df.rename(columns={'Port Name': 'Port_Name', 'Measure': 'Entry_Type'}, inplace=True)
#print(df.columns)

summary = df.groupby('Border')['Value'].sum()
#print(summary)

sorted_df = df.sort_values(by='Date', ascending=False)
#print(sorted_df[['Date', 'Border', 'Value']].head())

filtered_df = df[(df['Border'] == 'US-Canada Border') & (df['Value'] > 1000)]
#print(filtered_df)

q1=df['Value'].quantile(0.25)
q3=df['Value'].quantile(0.75)
IQR=q3-q1
lower_bond=q1-1.5*IQR
upper_bond=q3+1.5*IQR
Outlier=df[(df['Value']<lower_bond) | (df['Value']>upper_bond)]
#print(Outlier)

correlation=df.corr(numeric_only=True)
#print(correlation)

covariance=df.cov(numeric_only=True)
#print(covariance)



###Plot a time series line graph of total border crossings over time using the
##Date and Value columns. Customize the plot with a title, axis labels, rotated
##x-ticks, and a legend showing the border type.
df_grouped = df.groupby(['Date', 'Border'], as_index=False)['Value'].sum()
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_grouped, x='Date', y='Value', hue='Border', marker="o")
plt.title('Total Border Crossings Over Time by Border Type')
plt.xlabel('Date')
plt.ylabel('Number of Crossings')
plt.xticks(rotation=45)
plt.legend(title='Border Type')
plt.tight_layout()
plt.show()


##Perform an EDA on the dataset:
##Show the summary statistics (describe()) of numerical features.
###Compute and visualize the correlation between Value (number of crossings) and other relevant numeric features (e.g., time-based aggregation if applicable).

df["Date"]=pd.to_datetime(df["Date"],format='%b-%y')
correlation=df.corr(numeric_only=True)
print(correlation)
print("\n")
sns.heatmap(correlation,annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap - Value vs Other Features")
plt.show()
monthly_agg = df.groupby(df['Date'].dt.to_period('M'))['Value'].sum().reset_index()
monthly_agg['Date'] = monthly_agg['Date'].dt.to_timestamp()
sns.lineplot(data=monthly_agg, x='Date', y='Value')
plt.title('Monthly Total Border Crossings Over Time')
plt.xlabel('Date')
plt.ylabel('Total Crossings')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


##Analyze the monthly trend of border crossings by creating a time series plot of total crossings per month.


import matplotlib.pyplot as plt
df['Date'] = pd.to_datetime(df['Date'], format='%b-%y')
df['Month'] = df['Date'].dt.month
monthly_trends = df.groupby('Month')['Value'].sum()
plt.figure(figsize=(10, 6))
monthly_trends.plot(kind='line', marker='o')
plt.title('Monthly Border Crossing Trends')
plt.xlabel('Month')
plt.ylabel('Total Crossings')
plt.grid(True)
plt.show()



##Calculate the mean, median, and standard deviation of the Value column for the measure Trucks in the dataset.
##Perform a t-test to compare the mean Value of Trucks between the US-Canada Border and the US-Mexico Border.


trucks_data = df[df['Measure'] == 'Trucks']
mean_value = trucks_data['Value'].mean()
median_value = trucks_data['Value'].median()
std_value = trucks_data['Value'].std()
print(f"Mean: {mean_value}, Median: {median_value}, Std Dev: {std_value}")
canada_trucks = df[(df['Measure'] == 'Trucks') & (df['Border'] == 'US-Canada Border')]['Value']
mexico_trucks = df[(df['Measure'] == 'Trucks') & (df['Border'] == 'US-Mexico Border')]['Value']

t_stat, p_value = ttest_ind(canada_trucks, mexico_trucks, equal_var=False)

print(f"T-statistic: {t_stat}, P-value: {p_value}")



##Compare mean crossing values between January and April to see if there's a significant difference (simulated A/B test).

jan_data = df[df['Date'] == 'Jan-24']['Value']
apr_data = df[df['Date'] == 'Apr-24']['Value']
t_stat, p_val = ttest_ind(jan_data, apr_data, equal_var=False)

print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_val:.4f}")
alpha = 0.05
if p_val < alpha:
    print("Reject null hypothesis - significant difference between months")
else:
    print("Fail to reject null hypothesis - no significant difference")
