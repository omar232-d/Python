import pandas as pd

# Load CSV
df = pd.read_csv("data.csv")

# Show basic info
print("Data Loaded:\n", df)

# Group by department and calculate average salary
report = df.groupby("Department")["Salary"].mean().reset_index()

# Rename column
report.columns = ["Department", "Average Salary"]

# Save to Excel
report.to_excel("report.xlsx", index=False)

print("✅ Report generated: report.xlsx")