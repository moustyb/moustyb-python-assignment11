# Task 3: Interactive Visualizations with Plotly
import plotly.express as px
import plotly.data as pldata
import pandas as pd

# 1. Load the Plotly wind dataset
df = pldata.wind(return_type='pandas')

# Print the first and last 10 lines
print("First 10 rows:")
print(df.head(10), "\n")
print("Last 10 rows:")
print(df.tail(10), "\n")

# 2. Clean the data - convert 'strength' column to float
# The strength column has values like "6.0 m/s" so we need to extract just the number
df['strength'] = df['strength'].str.replace(r'[^\d.]', '', regex=True).astype(float)

print("Data after cleaning strength column:")
print(df[['strength', 'frequency', 'direction']].head(), "\n")

# 3. Create an interactive scatter plot of strength vs. frequency
# with colors based on the direction
fig = px.scatter(df, 
                 x='frequency', 
                 y='strength', 
                 color='direction',
                 title="Wind Strength vs Frequency by Direction",
                 labels={'frequency': 'Frequency', 
                        'strength': 'Strength (m/s)',
                        'direction': 'Wind Direction'},
                 hover_data=['direction'])

# 4. Save as HTML file
fig.write_html("wind.html", auto_open=True)

print("✅ Interactive plot saved to wind.html")
print("The plot should have opened automatically in your browser.")
