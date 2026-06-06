select e1. employee_id as employee_id,
e1.name,
count(e2.employee_id) as reports_count,
round(avg(e2.age)) as average_age
from Employees e1
join Employees e2
on e2.reports_to = e1.employee_id
group by e2.reports_to
order by e1.employee_id
