# Write your MySQL query statement below

select employee_id , IF(mod(employee_id,2)!=0 and left(name,1)!='M',(100/100.0)*(salary),0) as bonus
from Employees
order by  employee_id asc;