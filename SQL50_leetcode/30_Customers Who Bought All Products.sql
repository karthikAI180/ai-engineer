-- select c.customer_id
-- from (select customer_id,product_key, count(*) as Total_keys
-- from Customer
-- group by customer_id) c
-- left join Product p
-- on c.product_key=p.product_key 
-- having 
--  c.Total_keys=(select count(*) from product)

select customer_id
from Customer
group by customer_id
having count(distinct product_key) = (select count(*) from Product)
