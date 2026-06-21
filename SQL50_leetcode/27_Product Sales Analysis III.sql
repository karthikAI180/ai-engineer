select product_id, first_year,quantity,price
from
(select product_id,
year as first_year,
rank() over (partition by product_id order by year) as ranking,
quantity,
price
from sales) as k
where ranking=1

-- SELECT product_id, year AS first_year, quantity, price
-- FROM sales
-- WHERE (product_id, year) IN (
--     SELECT product_id, MIN(year)
--     FROM sales
--     GROUP BY product_id
