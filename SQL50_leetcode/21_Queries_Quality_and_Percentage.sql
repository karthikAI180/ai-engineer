select query_name, 
round(coalesce(avg(rating/position),0),2) as quality,
round(coalesce(sum(case when rating<3 then 1 end)/count(*)*100,0),2) as poor_query_percentage
from Queries
group by query_name