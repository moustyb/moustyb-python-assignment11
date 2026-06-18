import plotly.express as px
import plotly.data as pldata

# Load the wind dataset
df = pldata.wind(return_type='pandas')

# 1. Print first and last 10 lines to verify data load
print("First 10 lines:")
print(df.head(10))
print("\nLast 10 lines:")
print(df.tail(10))

# 2. Clean the data: convert 'strength' column to float
# Remove any non-numeric characters and convert to float
df['strength'] = df['strength'].str.replace(r'[^\d.]', '', regex=True).astype(float)

# 3 & 4. Create scatter plot with correct axes and colors
# x-axis = strength, y-axis = frequency, color = direction
fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title="Wind Strength vs Frequency by Direction",
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency', 'direction': 'Wind Direction'}
)

# Save the interactive plot to an HTML file
fig.write_html("wind.html", auto_open=True)
print("\nInteractive chart saved to wind.html")
