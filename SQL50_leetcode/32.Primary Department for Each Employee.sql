# Write your MySQL query statement below
select employee_id, department_id
from(
select employee_id,department_id, primary_flag,
count(department_id) over(partition by employee_id) as nd
from employee) k
where nd=1 or (nd>1 and primary_flag='Y')


-- SELECT employee_id, department_id
-- FROM employee
-- WHERE primary_flag = 'Y'
--    OR employee_id IN (
--        SELECT employee_id
--        FROM employee
--        GROUP BY employee_id
--        HAVING COUNT(*) = 1
--    )