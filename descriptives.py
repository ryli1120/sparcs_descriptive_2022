import requests
from io import StringIO
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url = ('https://health.data.ny.gov/resource/5dtw-tffi.csv')
response = requests.get(url)
data = StringIO(response.text)

#load dataset into Pandas
df = pd.read_csv(data)

print(df.columns)


# ***LENGTH OF STAY STATISTICS***
print("\n\n ***LENGTH OF STAY STATISTICS***")

#Convert length of stay parameters to numeric form
df['length_of_stay'] = pd.to_numeric(df['length_of_stay'], errors='coerce')

#LOS Mean
mean_LOS = df['length_of_stay'].mean()
print("\n Mean length of stay:", mean_LOS)

#LOS Median
median_LOS = df['length_of_stay'].median()
print("\n Median length of stay:", median_LOS)

#LOS std
std_LOS = df['length_of_stay'].std()
print("\n Standard deviation of length of stay:", std_LOS)

#LOS Min
min_LOS = df['length_of_stay'].min()
print("\n Minimum length of stay:", min_LOS)

#LOS Max
max_LOS = df['length_of_stay'].max()
print("\n Max length of stay:", max_LOS)

#LOS Q1
q1_los = df['length_of_stay'].quantile(0.25)
print("\n 25th Percentile (Q1) of length of stay:", q1_los)

#LOS Q2
q2_los = df['length_of_stay'].quantile(0.50)
print("\n 50th Percentile (Median, Q2) of length of stay:", q2_los)

#LOS Q3
q3_los = df['length_of_stay'].quantile(0.75)
print("\n 75th Percentile (Q3) of length of stay:", q3_los)

#LOS Histogram
plt.figure(figsize=(6, 4))
sns.histplot(df['length_of_stay'], bins=30, kde=True)
plt.title('Distribution of Length of Stay')
plt.xlabel('Length of Stay (Days)')
plt.ylabel('Frequency')
plt.show()



# ***TOTAL CHARGES STATISTICS***

#Fix formatting of total  costs parameters
df['total_charges'] = df['total_charges'].str.replace('[\$,]', '', regex=True)
df['total_charges'] = pd.to_numeric(df['total_charges'], errors='coerce')

# Total Charges Mean
mean_total_charges = df['total_charges'].mean()
print("\n\n ***TOTAL CHARGES STATISTICS***")
print("\n Mean total charges:", mean_total_charges)

# Total Charges Median
median_total_charges = df['total_charges'].median()
print("\n Median total charges:", median_total_charges)

# Total Charges Standard Deviation
std_total_charges = df['total_charges'].std()
print("\n Standard deviation of total charges:", std_total_charges)

# Total Charges Minimum
min_total_charges = df['total_charges'].min()
print("\n Minimum total charges:", min_total_charges)

# Total Charges Maximum
max_total_charges = df['total_charges'].max()
print("\n Max total charges:", max_total_charges)

# Total Charges Q1
q1_total_charges = df['total_charges'].quantile(0.25)
print("\n 25th Percentile (Q1) of total charges:", q1_total_charges)

# Total Charges Q2
q2_total_charges = df['total_charges'].quantile(0.50)
print("\n 50th Percentile (Median, Q2) of total charges:", q2_total_charges)

# Total Charges Q3
q3_total_charges = df['total_charges'].quantile(0.75)
print("\n 75th Percentile (Q3) of total charges:", q3_total_charges)

# Total Charges Box Plot 
plt.figure(figsize=(10, 6))  
sns.boxplot(x=df['total_charges'])  # Create the box plot
plt.title('Box Plot of Total Charges', fontsize=16)  # Title for the box plot
plt.xlabel('Total Charges', fontsize=14)  # X-axis label
plt.grid(axis='x')  # gridlines
plt.show()  # Show the plot



#***TOTAL COSTS STATISTICS***
print("\n\n ***TOTAL COSTS STATISTICS***")

#Fix formatting of total  costs parameters
df['total_costs'] = df['total_costs'].str.replace('[\$,]', '', regex=True)
df['total_costs'] = pd.to_numeric(df['total_costs'], errors='coerce')

# Total Costs Mean
mean_total_costs = df['total_costs'].mean()
print("\n\n")
print("\n Mean total costs:", mean_total_costs)

# Total Costs Median
median_total_costs = df['total_costs'].median()
print("\n Median total costs:", median_total_costs)

# Total Costs Standard Deviation
std_total_costs = df['total_costs'].std()
print("\n Standard deviation of total costs:", std_total_costs)

# Total Costs Minimum
min_total_costs = df['total_costs'].min()
print("\n Minimum total costs:", min_total_costs)

# Total Costs Maximum
max_total_costs = df['total_costs'].max()
print("\n Max total costs:", max_total_costs)

#Total Costs Q1
q1_total_costs = df['total_costs'].quantile(0.25)
print("\n 25th Percentile (Q1) of total costs:", q1_total_costs)

#Total Costs Q2
q2_total_costs = df['total_costs'].quantile(0.50)
print("\n 50th Percentile (Median, Q2) of total costs:", q2_total_costs)

#Total Costs Q3
q3_total_costs = df['total_costs'].quantile(0.75)
print("\n 75th Percentile (Q3) of total costs:", q3_total_costs)



# ***DISTRIBUTION OF AGE GROUP, GENDER, AND TYPE OF ADMISSION
age_group_count = df['age_group'].value_counts()
print("Age Group Distribution:\n", age_group_count)

gender_count = df['gender'].value_counts()
print("Gender Distribution:\n", gender_count)

type_of_admission_count = df['type_of_admission'].value_counts()
print("Type of Admission Distribution:\n", type_of_admission_count)



# ***BAR PLOT FOR TYPE OF ADMISSION***
#Group the data by Type of Admission and calculate the sum of Total Costs
admission_trends = df.groupby('type_of_admission')['total_costs'].sum()

#Create a bar plot 
plt.figure(figsize=(10, 6))  # Set figure size
admission_trends.plot(kind='bar', color='lightgreen')

plt.title('Total Costs by Type of Admission', fontsize=16)
plt.xlabel('Type of Admission', fontsize=14)
plt.ylabel('Total Costs', fontsize=14)
plt.xticks(rotation=45)  
plt.grid(axis='y')  

plt.show()


# ***SUMMARY***
print("\nThe averages length of stay is:", mean_LOS)
print("\nThe admission type with the highest costs is Emergency")
print("\nThere is a trend of a higher frequency during a lower length of stays")
