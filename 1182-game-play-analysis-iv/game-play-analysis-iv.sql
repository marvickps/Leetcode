# Write your MySQL query statement below
-- select
-- ROUND(
--     COUNT(DISTINCT a1.player_id)
--     / (SELECT COUNT(DISTINCT player_id) from activity)
--     ,2) as fraction
-- from Activity a1 left join activity a2 on a1.player_id = a2.player_id
-- where DATEDIFF(a2.event_date, a1.event_date ) = 1
-- order by a1.event_date asc

-- SELECT DISTINCT a.player_id, a.event_date, f.first_login from activity a inner join
--     ( select
--     player_id,
--     MIN(event_date) AS first_login
-- FROM Activity
-- GROUP BY player_id
--     ) f
--     on a.player_id = f.player_id
--     where datediff(a.event_date,f.first_login) = 1

SELECT 
ROUND(
    COUNT(DISTINCT a.player_id)
    / (select COUNT(distinct player_id) from activity)
    ,2) as fraction 
 from activity a inner join
    ( select
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id
    ) f
    on a.player_id = f.player_id
    where datediff(a.event_date,f.first_login) = 1