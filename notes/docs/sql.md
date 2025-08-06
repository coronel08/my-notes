# SQL

##

Example from timestream SQL with a CTE (Common Table Expression) and a window function with ROW_NUMBER()

```
WITH latest_records AS (
    SELECT
        site,
        uom,
        asset,
        time,
        measure_name,
        CASE
            WHEN measure_value::double IS NOT NULL THEN measure_value:double
            ELSE 0
        END as measure_value,
        ROW_NUMBER() OVER (
            PARTITION BY measure_name
            ORDER BY time DESC
        ) as rn
    FROM "DatabaseName"."TableName"
    WHERE time >= ago(1d)
        AND site = "ACY1"
        AND asset = "RTU_02"
)
SELECT
    site,
    uom,
    asset,
    time,
    measure_name,
    measure_value
FROM latest_records
WHERE rn = 1
ORDER BY measure_name
```

## Example of window functions

Window functions operate on a set of rows related to the current row.

Common window functions

-   ROW_NUMBER(): unique sequential number
-   RANK(): same value = same rank, skips same data
-   DENSE_RANK(): same value = same rank, no skipping
-   LAG()/LEAD(): access prev and next row
-   SUM()/AVG(): Calculate running totals/averages
-   FIRSt_VALUE()/LAST_VALUE(): get first/last value

Moving Average(Lag, Lead) example

```
WITH daily_sales AS (
    SELECT 'Mon' as day, 100 as sales
    UNION ALL SELECT 'Tue', 120
    UNION ALL SELECT 'Wed', 130
    UNION ALL SELECT 'Thu', 110
    UNION ALL SELECT 'Fri', 140
)
SELECT
    day,
    sales,
    LAG(sales) OVER (ORDER BY day) as previous_day_sales
    LEAD(sales) OVER (ORDER BY day) as next_day_sales
FROM daily_sales;

Result:
day |   sales |    prev_day |  next_day
Mon |   100   |    NULL     |   120
Tue |   120   |    100      |   130
Wed |   130   |    110      |   110
```

Running Totals using SUM and AVG window functions.

```
WITH monthly_sales as (
    SELECT 'Jan' as month, 100 as sales
    UNION ALL SELECT 'Feb', 200
    UNION ALL SELECT 'Mar', 150
    UNION ALL SELECT 'Apr', 300
)
SELECT
    month,
    sales,
    SUM(sales) OVER (ORDER BY month) as running_total,
    AVG(sales) OVER (ORDER by month) as running_avg
FROM monthly_sales;

Result:
montth  | sales |   running_total |     running_avg
Jan     |   100 |   100           |     100
Feb     | 200   |   300           |     150
Mar     | 150   |   450           |     150
```

Partitioning Example look into this more

```
WITH sales_by_region AS (
    SELECT 'North' as region, 'Jan' as month, 100 as sales
    UNION ALL SELECT 'North', 'Feb', 120
    UNION ALL SELECT 'South', 'Jan', 150
    Union ALL SELECT 'South', 'Feb', 160
)
SELECT
    region,
    month,
    sales,
    SUM(sales) OVER (PARTITION BY region) as region_total,
    AVG(sales) OVER (PARTITION BY region) as region_avg
FROM sales_by_region;

Result:
region  | month     |   sales   |   region_total    |   region_avg
North   | Jan       |   100     |   220             |   110
North   | Feb       |   120     |   220             |   110
South   | Jan       |   150     |   310             |   155
South   | Feb       |   160     |   310             |   155
```

## Example of Complex CTE

Common Table Expressions help organize complex queries into manageable pieces.

```
WITH monthly_sales as (
    SELECT 'Jan' as month, 100 as sales,
    UNION ALL SELECT 'Feb', 200
    UNION ALL SELECT 'Mar', 150
),
sales_stats AS
```
