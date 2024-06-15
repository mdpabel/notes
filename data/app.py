import pandas as pd

# Read the CSV file
df = pd.read_csv('employees.csv')

# Remove duplicate emails, keeping the first occurrence
df_cleaned = df.drop_duplicates(subset=['email'], keep='first')

# Save the cleaned data back to a CSV file
df_cleaned.to_csv('cleaned_employees.csv', index=False)
