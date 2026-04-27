# Write your MySQL query statement below
select p.product_id,
-- ROUND(IFNULL(
--     AVG(
        
-- ), 0),2) as u.average_price
ROUND(IFNULL(
    SUM(u.units * p.price)/SUM(u.units),
 0),2) as average_price
-- p.price
from prices p left join UnitsSold u
on p.product_id = u.product_id
AND u.purchase_date BETWEEN p.start_date and p.end_date
group by p.product_id