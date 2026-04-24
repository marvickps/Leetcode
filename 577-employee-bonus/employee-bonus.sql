# Write your MySQL query statement below
select em.name, bs.bonus from employee em left join bonus bs
on em.empId = bs.empId
where bs.bonus < 1000 or bs.bonus is null