# Write your MySQL query statement below
select reg.contest_id,
ROUND(COUNT( reg.user_id) * 100 / (SELECT COUNT(*) FROM users),2) as percentage 
from users u join register reg
on u.user_id = reg.user_id
group by reg.contest_id
order by percentage desc, reg.contest_id asc
