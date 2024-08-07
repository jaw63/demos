import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
df = pd.read_csv('jupiter data.csv')

# Ensure the Year_discovered column is numeric
df['Year_discovered'] = pd.to_numeric(df['Year_discovered'], errors='coerce')

# Drop rows with missing or invalid Year_discovered values
df = df.dropna(subset=['Year_discovered'])

# Sort the data by Year_discovered
df.sort_values('Year_discovered', inplace=True)

# Create a cumulative count of moons discovered
df['Cumulative_moons'] = range(1, len(df) + 1)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(df['Year_discovered'], df['Cumulative_moons'], marker='o')
plt.title('Cumulative Number of Known Moons of Jupiter Over Time')
plt.xlabel('Year Discovered')
plt.ylabel('Cumulative Number of Moons')
plt.grid(True)
plt.show()
