# Write your MySQL query statement below
with max_salary as (
    select max(salary) as salary
    from employee
)
select max(salary) as SecondHighestSalary
from employee
where salary < (select * from max_salary)