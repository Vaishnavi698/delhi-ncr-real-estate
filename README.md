# 🏙️ Delhi-NCR Real Estate Market & Price Fairness Analyzer

An end-to-end data analytics application and interactive dashboard that evaluates active real estate listings across the Delhi-NCR region. Powered by **DuckDB SQL** for high-performance analytical queries and **Streamlit** for real-time visualization, this project benchmarks locality pricing, identifies overpriced/underpriced listings, and visualizes regional property trends.

---

## 📌 Problem Statement & Core Objective

The Delhi-NCR real estate market is vast and fragmented, making it difficult for buyers and analysts to determine whether a property is priced fairly. Key challenges include:
- **Price Mismatches:** Sellers listing properties far above or below market value.
- **Lack of Micro-Market Benchmarks:** Difficulty comparing property rates (₹/sq.ft) against local area averages.
- **Unstructured Data:** Raw listing datasets with missing values (e.g., missing furnishing status) and inconsistent price formats.

### The Solution
This app standardizes raw property data, calculates baseline benchmarks per locality and BHK configuration using DuckDB SQL, and automatically flags listings deviating by more than ±20% from market medians.

---

## 🛠️ Data Cleaning & Processing Pipeline

1. **Data Ingestion:** Extracted property records across major Delhi-NCR sub-regions (Delhi, Gurgaon, Noida, Greater Noida, Ghaziabad, Faridabad).
2. **Currency Standardization:** Converted raw prices into readable Indian Rupee formats (Lakhs and Crores).
3. **Missing Value Handling:** Replaced blank/missing furnishing values (`nan`) with `"Not Specified"` for cleaner presentation.
4. **Derived Metrics:** Calculated `Price_per_SqFt`, `Avg_Price` per locality/BHK, and generated dynamic `Price_Tag` classifications (*Fair Market Price*, *Overpriced*, *Underpriced*).

---

## ⚡ Analytics Engine: DuckDB SQL Transformations

The backend uses **DuckDB SQL** to perform high-speed OLAP aggregations.

### 1. Locality & BHK Pricing Benchmarks
```sql
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

2. Flagging Price Mismatches (>20% Deviation)SQLSELECT 
    l.Locality,
    l.BHK,
    l.Area,
    l.Price AS Listed_Price,
    b.Avg_Price AS Locality_Avg_Price,
    CASE 
        WHEN l.Price > (b.Avg_Price * 1.20) THEN 'Overpriced (>20%)'
        WHEN l.Price < (b.Avg_Price * 0.80) THEN 'Underpriced (>20%)'
        ELSE 'Fair Market Price'
    END AS Price_Tag
FROM listings l
JOIN locality_benchmarks b 
  ON l.Locality = b.Locality AND l.BHK = b.BHK;
⚠️ Challenges Faced & SolutionsHandling Missing Values (nan string issues):Problem: Pandas filled missing furnishing status with nan, which appeared raw on dashboard cards.Solution: Applied explicit string cleaning and .fillna('Not Specified') logic.Large Price Range Representation:Problem: Comparing ₹40 Lakh flats with ₹15 Crore luxury homes skewed visual charts.Solution: Implemented helper functions to dynamically scale numbers to ₹ Lakh ($10^5$) and ₹ Cr ($10^7$) and used Plotly log/scaled axes where appropriate.📸 Dashboard Previews🏙️ Dashboard Overview📌 1. Locality Deep-Dive & Scatter Analysis🏠 2. BHK Price Breakdown Chart💡 3. Budget Options & Flagged Mismatches🚩 4. Benchmark Drilldown Data Table🌆 5. Top Premium Localities💰 6. Top Affordable Localities💻 7. Embedded DuckDB SQL Engine🛠️ Tech Stack UsedLanguage: Python 3.10+Database Engine: DuckDB (SQL OLAP)Data Manipulation: Pandas, NumPyVisualizations: Plotly ExpressWeb App Framework: StreamlitVersion Control & Hosting: Git, GitHub, Streamlit Community Cloud🚀 How to Run LocallyBash# Clone repository
git clone [https://github.com/Vaishnavi698/delhi-ncr-real-estate.git](https://github.com/Vaishnavi698/delhi-ncr-real-estate.git)

# Navigate to folder
cd delhi-ncr-real-estate

# Install dependencies
pip install -r requirements.txt

# Run Streamlit App
streamlit run app.py

---

### Terminal Commands to Push to GitHub

Once you save `README.md`, run these commands in your VS Code terminal to send all the images and the updated `README.md` to GitHub:

```powershell
git add .
git commit -m "Update README.md with root image references"
git push origin main
