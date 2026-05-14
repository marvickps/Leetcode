# Write your MySQL query statement below

-- x = delivery_id = customer_pref_delivery_date = immediate ? scheduled
-- y = order by date asc limit 1 / Top 1 * from __ order by date asc  =  first order DONE
-- x/y*100

-- Select * from (
--     Select customer_id, order_date, customer_pref_delivery_date,
--     ROW_NUMBER() 
--         OVER (
--             PARTITION BY customer_id
--             ORDER BY order_date asc) as rn
--         from delivery 
--     ) tabe
--         where rn = 1

Select 
 ROUND(
 AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1 ELSE 0 END) * 100.0, 2) as immediate_percentage 
 from (
    Select customer_id, order_date, customer_pref_delivery_date,
    ROW_NUMBER() 
        OVER (
            PARTITION BY customer_id
            ORDER BY order_date asc) as rn
        from delivery 
    ) tabe
        where rn = 1