# 🏙️ Delhi-NCR Real Estate Market & Price Fairness Analyzer

An end-to-end data analytics application and interactive dashboard that evaluates active real estate listings across the Delhi-NCR region. Powered by **DuckDB SQL** for high-performance analytical queries and **Streamlit** for real-time visualization, this project benchmarks locality pricing, identifies overpriced/underpriced listings, and visualizes regional property trends.

---

## 📌 Problem Statement & Core Objective

The Delhi-NCR real estate market is vast and fragmented, making it difficult for buyers and analysts to determine whether a property is priced fairly. Key challenges include:
- **Price Mismatches:** Sellers listing properties far above or below market value.
- **Lack of Micro-Market Benchmarks:** Difficulty comparing property rates ($\text{₹/sq.ft}$) against local area averages.
- **Unstructured Data:** Raw listing datasets with missing values (e.g., missing furnishing status) and inconsistent price formats.

### The Solution
This app standardizes raw property data, calculates baseline benchmarks per locality and BHK configuration using DuckDB SQL, and automatically flags listings deviating by more than $\pm20\%$ from market medians.

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