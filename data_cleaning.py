import pandas as pd
import duckdb

# 1. Load Data
df = pd.read_csv('data/MagicBricks.csv')

# Drop unnecessary index column if present
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# Clean column names for consistency
df = df.rename(columns={
    'Address': 'Locality',
    'price': 'Price',
    'area': 'Area',
    'Bedrooms': 'BHK'
})

# 2. Basic Cleaning
df = df.dropna(subset=['Price', 'Locality', 'Area', 'BHK'])

# Convert columns to numeric if needed
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['Area'] = pd.to_numeric(df['Area'], errors='coerce')
df['BHK'] = pd.to_numeric(df['BHK'], errors='coerce')
df['Price_per_SqFt'] = df['Price'] / df['Area']

# 3. DuckDB SQL Query for Locality Benchmarks
con = duckdb.connect()
con.register('listings', df)

query = """
SELECT 
    Locality,
    BHK,
    ROUND(AVG(Price), 2) AS Avg_Price,
    ROUND(AVG(Price_per_SqFt), 2) AS Avg_Price_Per_SqFt,
    COUNT(*) AS Listing_Count
FROM listings
GROUP BY Locality, BHK
HAVING COUNT(*) >= 2
"""
locality_benchmarks = con.execute(query).df()

# Merge benchmarks back onto original listings
df_merged = pd.merge(df, locality_benchmarks, on=['Locality', 'BHK'], suffixes=('', '_Locality_Avg'))

# 4. Overpriced / Underpriced Logic
def flag_price(row):
    if pd.isna(row['Avg_Price']) or row['Avg_Price'] == 0:
        return 'No Benchmark Data'
    ratio = row['Price'] / row['Avg_Price']
    if ratio > 1.20:
        return 'Overpriced (>20% above avg)'
    elif ratio < 0.80:
        return 'Underpriced (>20% below avg)'
    else:
        return 'Fair Market Price'

df_merged['Price_Tag'] = df_merged.apply(flag_price, axis=1)

# Save cleaned output
df_merged.to_csv('data/cleaned_delhi_real_estate.csv', index=False)
print("Data cleaning & DuckDB SQL aggregation completed successfully!")
print(f"Processed {len(df_merged)} listings saved to data/cleaned_delhi_real_estate.csv")