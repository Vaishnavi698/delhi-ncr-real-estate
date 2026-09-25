import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Delhi-NCR Real Estate Market Analyzer", layout="wide")

@st.cache_data
def load_data():
    return pd.read_csv('data/cleaned_delhi_real_estate.csv')

df = load_data()

# INR Currency Formatting Helper
def format_inr(number):
    if pd.isna(number):
        return "N/A"
    if number >= 10_000_000:
        return f"₹{number / 10_000_000:.2f} Cr"
    elif number >= 100_000:
        return f"₹{number / 100_000:.2f} Lakh"
    else:
        return f"₹{number:,.0f}"

# Title Header
st.title("🏙️ Delhi-NCR Real Estate Market & Price Fairness Analyzer")
st.markdown(
    "*Comparing active listings against locality benchmarks to flag fair, overpriced, and underpriced properties across Delhi-NCR.*"
)

# Sidebar Controls
st.sidebar.header("🔍 Filter Options")
localities = sorted(df['Locality'].dropna().unique())
selected_locality = st.sidebar.selectbox("Select Locality", localities)

bhk_options = sorted([int(b) for b in df['BHK'].dropna().unique()])
selected_bhk = st.sidebar.multiselect("Select BHK Type", bhk_options, default=bhk_options)

# Filter Dataset
filtered_df = df[(df['Locality'] == selected_locality) & (df['BHK'].isin(selected_bhk))]

# Main Tabs (Structuring Dashboard for Interviewers)
tab1, tab2, tab3 = st.tabs(["📌 Locality Deep-Dive", "🌆 Regional Price Trends", "💻 DuckDB SQL Queries"])

# ==================== TAB 1: LOCALITY ANALYSIS ====================
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Selected Locality", selected_locality.split(',')[0])
    col2.metric("Average Price", format_inr(filtered_df['Price'].mean()) if len(filtered_df) > 0 else "N/A")
    col3.metric("Avg Rate / Sq.Ft", f"₹{filtered_df['Price_per_SqFt'].mean():,.0f}" if len(filtered_df) > 0 else "N/A")
    col4.metric("Listings Found", len(filtered_df))

    st.markdown("---")

    if len(filtered_df) > 0:
        # Scatter Chart: Price vs Area
        st.subheader(f"📊 Property Price vs. Size in {selected_locality.split(',')[0]}")
        fig_scatter = px.scatter(
            filtered_df, 
            x='Area', 
            y='Price', 
            color='Price_Tag',
            size='BHK',
            hover_data=['Furnished_status', 'Status', 'type_of_building'],
            color_discrete_map={
                'Fair Market Price': '#2ecc71',
                'Overpriced (>20% above avg)': '#e74c3c',
                'Underpriced (>20% below avg)': '#3498db'
            }
        )
        st.plotly_chart(fig_scatter, use_container_width=True)

        # BHK Price Breakdown Bar Chart
        st.subheader("🏠 Average Price Breakdown by BHK Type")
        bhk_summary = filtered_df.groupby('BHK')['Price'].mean().reset_index()
        bhk_summary['Price_Formatted'] = bhk_summary['Price'].apply(format_inr)
        
        fig_bhk = px.bar(
            bhk_summary,
            x='BHK',
            y='Price',
            text='Price_Formatted',
            title=f"BHK Pricing Structure in {selected_locality.split(',')[0]}",
            labels={'Price': 'Average Price (₹)', 'BHK': 'BHK Type'},
            color='Price',
            color_continuous_scale='Blues'
        )
        st.plotly_chart(fig_bhk, use_container_width=True)

      # Cheapest Options Section
        st.subheader("💡 Cheapest Available Options in Locality")
        cheapest_df = filtered_df.sort_values(by='Price').head(3)
        cols = st.columns(len(cheapest_df))
        for idx, (_, row) in enumerate(cheapest_df.iterrows()):
            # Handle NaN furnishing status gracefully
            furnishing = row['Furnished_status']
            if pd.isna(furnishing) or str(furnishing).lower() == 'nan':
                furnishing = "Not Specified"

            with cols[idx]:
                st.info(
                    f"**{int(row['BHK'])} BHK — {row['Area']} sq.ft.**\n\n"
                    f"• **Price:** {format_inr(row['Price'])}\n\n"
                    f"• **Rate:** ₹{row['Price_per_SqFt']:,.0f} / sq.ft\n\n"
                    f"• **Status:** {furnishing}"
                )

        # Table of Flagged Mismatches
        st.subheader("🚩 Flagged Listings (Fair vs Overpriced Mismatches)")
        display_df = filtered_df[['Locality', 'BHK', 'Area', 'Price', 'Avg_Price', 'Price_per_SqFt', 'Price_Tag']].copy()
        display_df['Listed Price'] = display_df['Price'].apply(format_inr)
        display_df['Locality Benchmark'] = display_df['Avg_Price'].apply(format_inr)
        
        st.dataframe(
            display_df[['Locality', 'BHK', 'Area', 'Listed Price', 'Locality Benchmark', 'Price_per_SqFt', 'Price_Tag']],
            use_container_width=True
        )
    else:
        st.warning("No properties match the selected filters.")

# ==================== TAB 2: REGIONAL TRENDS ====================
with tab2:
    st.subheader("🌆 Delhi-NCR Locality Price Rankings")
    
    # Top 10 Most Expensive
    top_10 = (
        df.groupby('Locality')
        .agg(Avg_Rate=('Price_per_SqFt', 'mean'), Listings=('Price', 'count'))
        .query('Listings >= 3')
        .sort_values(by='Avg_Rate', ascending=False)
        .head(10)
        .reset_index()
    )

    fig_top = px.bar(
        top_10,
        x='Avg_Rate',
        y='Locality',
        orientation='h',
        title="Top 10 Premium Localities (Avg Rate / Sq.Ft)",
        labels={'Avg_Rate': 'Avg Price/Sq.Ft (₹)'},
        color='Avg_Rate',
        color_continuous_scale='Reds'
    )
    st.plotly_chart(fig_top, use_container_width=True)

    # Top 10 Most Affordable
    st.subheader("💰 Top 10 Affordable Localities")
    bottom_10 = (
        df.groupby('Locality')
        .agg(Avg_Rate=('Price_per_SqFt', 'mean'), Listings=('Price', 'count'))
        .query('Listings >= 3')
        .sort_values(by='Avg_Rate', ascending=True)
        .head(10)
        .reset_index()
    )

    fig_bottom = px.bar(
        bottom_10,
        x='Avg_Rate',
        y='Locality',
        orientation='h',
        title="Top 10 Most Affordable Localities (Avg Rate / Sq.Ft)",
        labels={'Avg_Rate': 'Avg Price/Sq.Ft (₹)'},
        color='Avg_Rate',
        color_continuous_scale='Greens'
    )
    st.plotly_chart(fig_bottom, use_container_width=True)

# ==================== TAB 3: DUCKDB SQL LOGIC ====================
with tab3:
    st.subheader("⚡ DuckDB SQL Aggregation & Benchmarking Logic")
    st.markdown("Below are the exact SQL queries executed in Python via `DuckDB` to benchmark market averages and generate price tags:")

    st.code("""
-- Query 1: Calculate Locality & BHK Benchmarks
SELECT 
    Locality,
    BHK,
    ROUND(AVG(Price), 2) AS Avg_Price,
    ROUND(AVG(Price_per_SqFt), 2) AS Avg_Price_Per_SqFt,
    COUNT(*) AS Listing_Count
FROM listings
GROUP BY Locality, BHK
HAVING COUNT(*) >= 2;
    """, language="sql")

    st.code("""
-- Query 2: Identify Overpriced / Underpriced Properties (>20% Deviation)
SELECT 
    l.Locality,
    l.BHK,
    l.Price AS Listed_Price,
    b.Avg_Price AS Locality_Avg_Price,
    CASE 
        WHEN l.Price > (b.Avg_Price * 1.20) THEN 'Overpriced'
        WHEN l.Price < (b.Avg_Price * 0.80) THEN 'Underpriced'
        ELSE 'Fair Market Price'
    END AS Price_Tag
FROM listings l
JOIN locality_benchmarks b 
  ON l.Locality = b.Locality AND l.BHK = b.BHK;
    """, language="sql")