# 🏙️ Delhi-NCR Real Estate Market & Price Fairness Analyzer

> **An end-to-end data analytics project that turns raw Delhi-NCR
> property listings into actionable market insights using Python, DuckDB
> SQL, Pandas, Plotly, and Streamlit.**

```{=html}
<p align="center">
```
`<a href="https://vaishnavi698-delhi-ncr-real-estate-app-6cwu4s.streamlit.app/">`{=html}
`<strong>`{=html}🚀 OPEN LIVE STREAMLIT DASHBOARD`</strong>`{=html}
`</a>`{=html}
```{=html}
</p>
```
```{=html}
<p align="center">
```
`<img src="screenshots/dashboard_overview.png.png" alt="Delhi-NCR Real Estate Dashboard Overview" width="900">`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 🎯 What This Project Does

The Delhi-NCR real estate market is highly fragmented. Property prices
can vary significantly by **locality, BHK configuration, area, and
region**, making it difficult to judge a listing from its asking price
alone.

This project builds an interactive analytics application that:

-   📍 compares prices across localities
-   🏠 analyzes BHK-wise pricing patterns
-   📐 evaluates price per square foot
-   💰 surfaces comparatively affordable listings
-   🚩 flags listings that deviate significantly from their benchmark
-   🌆 compares regional price trends
-   💻 uses DuckDB SQL for analytical transformations
-   📊 presents the results through an interactive Streamlit dashboard

### 🔗 Live Application

**[👉 Launch the Interactive Streamlit
Dashboard](https://vaishnavi698-delhi-ncr-real-estate-app-6cwu4s.streamlit.app/)**

The live application lets you interact with filters, charts, benchmark
analysis, flagged listings, and drilldown tables.

------------------------------------------------------------------------

## 📌 Problem Statement

A property listing's price is difficult to evaluate without comparable
market context.

### Key Challenges

  -----------------------------------------------------------------------
  Challenge                           Why it matters
  ----------------------------------- -----------------------------------
  💸 Price mismatch                   Asking prices may differ
                                      substantially from comparable
                                      listings

  📍 Locality variation               Different micro-markets can have
                                      very different price levels

  🏠 BHK differences                  Different configurations require
                                      relevant comparison groups

  📊 Unstructured data                Raw listings can contain missing
                                      and inconsistent values

  📈 Wide price range                 Budget and luxury properties create
                                      difficult visual comparisons
  -----------------------------------------------------------------------

### 💡 Approach

The application standardizes raw listing data, creates **Locality + BHK
benchmarks**, calculates derived metrics, and classifies listings based
on deviation from the relevant benchmark.

-   🔴 **Overpriced (\>20%)**
-   🟢 **Underpriced (\>20%)**
-   🟡 **Fair Market Price**

> **Note:** These are analytical classifications based on the project's
> benchmark methodology, not professional property valuations.

------------------------------------------------------------------------

## 🔄 Data Analytics Pipeline

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td align="center">
```
`<strong>`{=html}1️⃣ Raw Listings`</strong>`{=html}`<br>`{=html}Property
Data
```{=html}
</td>
```
```{=html}
<td align="center">
```
→
```{=html}
</td>
```
```{=html}
<td align="center">
```
`<strong>`{=html}2️⃣ Data
Cleaning`</strong>`{=html}`<br>`{=html}Standardization
```{=html}
</td>
```
```{=html}
<td align="center">
```
→
```{=html}
</td>
```
```{=html}
<td align="center">
```
`<strong>`{=html}3️⃣ Feature
Engineering`</strong>`{=html}`<br>`{=html}Derived Metrics
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td align="center">
```
`<strong>`{=html}4️⃣ DuckDB
SQL`</strong>`{=html}`<br>`{=html}Aggregations
```{=html}
</td>
```
```{=html}
<td align="center">
```
→
```{=html}
</td>
```
```{=html}
<td align="center">
```
`<strong>`{=html}5️⃣ Benchmarks`</strong>`{=html}`<br>`{=html}Locality +
BHK
```{=html}
</td>
```
```{=html}
<td align="center">
```
→
```{=html}
</td>
```
```{=html}
<td align="center">
```
`<strong>`{=html}6️⃣ Price
Analysis`</strong>`{=html}`<br>`{=html}Deviation Flags
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td align="center">
```
`<strong>`{=html}7️⃣ Streamlit`</strong>`{=html}`<br>`{=html}Interactive
Dashboard
```{=html}
</td>
```
```{=html}
<td align="center">
```
→
```{=html}
</td>
```
```{=html}
<td align="center">
```
`<strong>`{=html}8️⃣ Insights`</strong>`{=html}`<br>`{=html}Market
Analysis
```{=html}
</td>
```
```{=html}
<td>
```
```{=html}
</td>
```
```{=html}
<td>
```
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```

------------------------------------------------------------------------

## 🛠️ Data Cleaning & Processing

The raw property dataset is processed before analytical queries and
visualization.

### 1. Data Ingestion

Property records cover major Delhi-NCR markets:

**Delhi • Gurgaon • Noida • Greater Noida • Ghaziabad • Faridabad**

### 2. Price Standardization

Prices are converted into numerical values and presented in readable
Indian formats:

**₹ Lakhs • ₹ Crores**

### 3. Missing Value Handling

Missing furnishing values are cleaned and displayed as:

`Not Specified`

### 4. Derived Metrics

The pipeline generates:

-   `Price_per_SqFt`
-   `Avg_Price`
-   Locality-level benchmarks
-   BHK-level benchmarks
-   `Price_Tag`

------------------------------------------------------------------------

## 📍 1. Locality Deep-Dive

The locality analysis provides a detailed view of property pricing
across Delhi-NCR micro-markets.

```{=html}
<p align="center">
```
`<img src="screenshots/01_locality_deep_dive.png" alt="Locality Deep Dive" width="900">`{=html}
```{=html}
</p>
```
**Focus:** locality, property area, listed price, price per sq.ft, and
comparable market context.

------------------------------------------------------------------------

## 🏠 2. BHK Price Breakdown

Pricing patterns can differ substantially by property configuration.

```{=html}
<p align="center">
```
`<img src="screenshots/02_bhk_price_breakdown.png" alt="BHK Price Breakdown" width="900">`{=html}
```{=html}
</p>
```
The analysis compares BHK configuration, average property price,
property size, price per sq.ft, and listing volume.

------------------------------------------------------------------------

## 💰 3. Affordable Options & Flagged Listings

This section combines comparatively affordable listings with properties
that show significant deviation from their benchmark.

```{=html}
<p align="center">
```
`<img src="screenshots/03_cheapest_options_and_flagged.png" alt="Affordable Options and Flagged Listings" width="900">`{=html}
```{=html}
</p>
```
  Classification         Rule
  ---------------------- -----------------------------------
  🔴 Overpriced          Listed price \> 120% of benchmark
  🟢 Underpriced         Listed price \< 80% of benchmark
  🟡 Fair Market Price   Within ±20% of benchmark

------------------------------------------------------------------------

## 🌆 4. Regional Price Trends

The dashboard compares observed property pricing across Delhi-NCR
regions.

```{=html}
<p align="center">
```
`<img src="screenshots/04_regional_price_trends.png" alt="Regional Price Trends" width="900">`{=html}
```{=html}
</p>
```
This provides a regional view of pricing variation across major
Delhi-NCR markets.

------------------------------------------------------------------------

## 💻 5. DuckDB SQL Analytics Engine

DuckDB is used as the analytical SQL engine for aggregation,
benchmarking, and price-deviation analysis.

```{=html}
<p align="center">
```
`<img src="screenshots/05_duckdb_sql_queries.png" alt="DuckDB SQL Queries" width="900">`{=html}
```{=html}
</p>
```
### Locality & BHK Pricing Benchmarks

``` sql
SELECT 
    Locality,
    BHK,
    ROUND(AVG(Price), 2) AS Avg_Price,
    ROUND(AVG(Price_per_SqFt), 2) AS Avg_Price_Per_SqFt,
    COUNT(*) AS Listing_Count
FROM listings
GROUP BY Locality, BHK
HAVING COUNT(*) >= 2
ORDER BY Avg_Price DESC;
```

### 🚩 Price Deviation Detection

``` sql
SELECT 
    l.Locality,
    l.BHK,
    l.Area,
    l.Price AS Listed_Price,
    b.Avg_Price AS Locality_Avg_Price,
    CASE 
        WHEN l.Price > (b.Avg_Price * 1.20) 
            THEN 'Overpriced (>20%)'
        WHEN l.Price < (b.Avg_Price * 0.80) 
            THEN 'Underpriced (>20%)'
        ELSE 'Fair Market Price'
    END AS Price_Tag
FROM listings l
JOIN locality_benchmarks b 
    ON l.Locality = b.Locality
    AND l.BHK = b.BHK;
```

------------------------------------------------------------------------

## 💡 6. Affordable Regional Markets

A dedicated view highlights comparatively affordable regional price
trends.

```{=html}
<p align="center">
```
`<img src="screenshots/05_regional_price_trends_affordable.png" alt="Affordable Regional Price Trends" width="900">`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## 📋 7. Benchmark Drilldown

The drilldown table exposes the underlying benchmark and listing-level
results behind the visualizations.

```{=html}
<p align="center">
```
`<img src="screenshots/drilldown_table.png.png" alt="Benchmark Drilldown Table" width="900">`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## ⚠️ Challenges Faced & Solutions

### 1. Missing Values

**Problem:** Missing furnishing values could appear as raw `NaN` values.

**Solution:** Explicitly handled missing values and displayed them as
`Not Specified`.

``` python
df["Furnishing"] = df["Furnishing"].fillna("Not Specified")
```

### 2. Large Price Range

**Problem:** The dataset spans a wide price range.

**Solution:** Prices are formatted dynamically using **₹ Lakhs** and **₹
Crores**, with appropriate chart scaling where required.

### 3. Locality-Level Comparability

**Problem:** A single overall market average can hide major differences
between localities.

**Solution:** Benchmarks are calculated at the **Locality + BHK** level.

------------------------------------------------------------------------

## 📈 Key Analytical Questions

-   Which localities have higher or lower observed property prices?
-   How does pricing vary across BHK configurations?
-   What is the average price per sq.ft across localities?
-   Which listings deviate significantly from their locality/BHK
    benchmark?
-   Which regions contain comparatively affordable options?
-   How does property area relate to listing price?
-   How can SQL-based benchmarking provide additional context around
    asking prices?

------------------------------------------------------------------------

## 🧰 Tech Stack

  Technology                         Purpose
  ---------------------------------- -----------------------------------
  🐍 **Python 3.10+**                Core programming language
  🦆 **DuckDB**                      Analytical SQL / OLAP engine
  🐼 **Pandas**                      Data cleaning & manipulation
  🔢 **NumPy**                       Numerical operations
  📊 **Plotly Express**              Interactive visualizations
  🎈 **Streamlit**                   Interactive web application
  🌐 **GitHub**                      Version control & project hosting
  ☁️ **Streamlit Community Cloud**   Deployment

------------------------------------------------------------------------

## 📁 Project Structure

``` text
delhi-ncr-real-estate/
│
├── app.py
├── data_cleaning.py
├── queries.sql
├── requirements.txt
├── README.md
│
├── data/
│   └── ...
│
└── screenshots/
    ├── 01_locality_deep_dive.png
    ├── 02_bhk_price_breakdown.png
    ├── 03_cheapest_options_and_flagged.png
    ├── 04_regional_price_trends.png
    ├── 05_duckdb_sql_queries.png
    ├── 05_regional_price_trends_affordable.png
    ├── dashboard_overview.png.png
    └── drilldown_table.png.png
```

------------------------------------------------------------------------

## 🚀 Run Locally

### 1. Clone the repository

``` bash
git clone https://github.com/Vaishnavi698/delhi-ncr-real-estate.git
```

### 2. Navigate to the project

``` bash
cd delhi-ncr-real-estate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Launch the Streamlit dashboard

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

## 🚀 Try the Live Application

```{=html}
<p align="center">
```
`<a href="https://vaishnavi698-delhi-ncr-real-estate-app-6cwu4s.streamlit.app/">`{=html}
`<strong>`{=html}🔴 LAUNCH LIVE STREAMLIT DASHBOARD →`</strong>`{=html}
`</a>`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

## ⭐ Project Highlights

  -----------------------------------------------------------------------
  Area                                Highlights
  ----------------------------------- -----------------------------------
  📊 **Data Analytics**               Cleaning, transformation, feature
                                      engineering, price analysis

  💻 **SQL**                          DuckDB, aggregations, benchmarks,
                                      joins, CASE logic

  📈 **Visualization**                Plotly charts, regional trends, BHK
                                      analysis

  🚩 **Price Analysis**               Locality + BHK benchmark deviation

  🎈 **Application**                  Interactive Streamlit dashboard

  🚀 **Deployment**                   Live Streamlit Community Cloud
                                      application
  -----------------------------------------------------------------------

------------------------------------------------------------------------

## 👩‍💻 Author

### Vaishnavi Gupta

**Computer Science Graduate \| Data Analytics \| Python \| SQL \| DuckDB
\| Power BI \| Streamlit**

```{=html}
<p align="center">
```
`<strong>`{=html}🏙️ Turning property listings into structured,
benchmark-driven insights.`</strong>`{=html}
```{=html}
</p>
```
