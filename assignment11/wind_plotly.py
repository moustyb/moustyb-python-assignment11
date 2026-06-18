import plotly.express as px
import pandas as pd

print("🚀 Starting Task 3: Plotly Wind Scatter Plot...")

# 1. Load the built-in wind dataset
df = px.data.wind()
print(f"✅ Successfully loaded wind dataset with {len(df)} rows")

# 2. Clean the data
# Map text ranges to numbers for the 'size' property
strength_map = {'0-1': 1, '2-3': 3, '4-5': 5, '6-7': 7, '8-9': 9}
df['strength_num'] = df['strength'].map(strength_map)

# IMPORTANT: Drop any rows where the conversion failed (NaN values)
df = df.dropna(subset=['strength_num'])
print(f"✅ Cleaned data: {len(df)} rows remaining after removing invalid data")

# 3. Create the scatter plot
# We use 'strength_num' for size (must be numbers) and 'strength' for color
fig = px.scatter(
    df, 
    x="direction", 
    y="frequency", 
    color="strength", 
    size="strength_num",
    title="Wind Direction and Frequency"
)

# 4. Save the plot as an HTML file
try:
    fig.write_html("wind.html")
    print("✅ Successfully saved interactive chart to 'wind.html'")
except Exception as e:
    print(f"❌ FAILED to save chart: {e}")

print("✅ Task 3 completed successfully!")