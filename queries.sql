-- Delhi-NCR Real Estate Market Benchmarking Queries (DuckDB SQL)

-- 1. Locality & BHK Pricing Benchmarks
SELECT 
    Locality,
    BHK,
    ROUND(AVG(Price), 2) AS Avg_Price,
    ROUND(AVG(Price_per_SqFt), 2) AS Avg_Price_Per_SqFt,
    COUNT(*) AS Total_Listings
FROM listings
GROUP BY Locality, BHK
HAVING COUNT(*) >= 2
ORDER BY Avg_Price DESC;

-- 2. Flag Overpriced (>20% above avg) and Underpriced (>20% below avg) Listings
SELECT 
    l.Locality,
    l.BHK,
    l.Area,
    l.Price AS Listed_Price,
    b.Avg_Price AS Locality_Avg_Price,
    ROUND((l.Price / b.Avg_Price) * 100, 1) AS Price_To_Avg_Percentage,
    CASE 
        WHEN l.Price > (b.Avg_Price * 1.20) THEN 'Overpriced (>20%)'
        WHEN l.Price < (b.Avg_Price * 0.80) THEN 'Underpriced (>20%)'
        ELSE 'Fair Market Value'
    END AS Price_Tag
FROM listings l
JOIN locality_benchmarks b 
  ON l.Locality = b.Locality AND l.BHK = b.BHK;