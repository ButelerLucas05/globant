
-- PRIMER PUNTO
with tmp as (
	select 
	dep.department as department,
	jb.job as job,
	case
		when EXTRACT('MONTH' FROM emp.datetime) in (1,2,3) then 1
		when EXTRACT('MONTH' FROM emp.datetime) in (4,5,6) then 2
		when EXTRACT('MONTH' FROM emp.datetime) in (7,8,9) then 3
		when EXTRACT('MONTH' FROM emp.datetime) in (10,11,12) then 4
	end as quarter
	from employees emp
	left join departments dep on dep.id = emp.department_id
	left join jobs jb on jb.id = emp.job_id
)
select department,
	   job,
	   sum(case when quarter = 1 then 1 else 0 end ) as q1,
	   sum(case when quarter = 2 then 1 else 0 end ) as q2,
	   sum(case when quarter = 3 then 1 else 0 end ) as q3,
	   sum(case when quarter = 4 then 1 else 0 end ) as q4
from tmp
group by department,job
order by department,job asc ;



-- SEGUNDO PUNTO


SELECT 
    d.id AS department_id, 
    d.department, 
    COUNT(e.id) AS number_of_employees_hired
FROM departments d
JOIN employees e ON d.id = e.department_id
-- Aca me quedo la duda de si se deben contar todos los contratados por mas que no sean en 2021 (teniendo en cuenta como filtro solo la media de 2021)
-- Si la idea es que solo se tengan en cuenta los empleados de 2021 , hay que descomentar la linea de abajo.
--WHERE  EXTRACT('YEAR' FROM e.datetime) = '2021'  
GROUP BY d.id, d.department
HAVING COUNT(e.id) > (SELECT AVG(num_employees_hired) 
                        FROM   (SELECT COUNT(id) AS num_employees_hired FROM employees 
                        -- Obtenemos la media de contrataciones del 2021
                        WHERE  EXTRACT('YEAR' FROM datetime) = '2021'  
                        GROUP BY department_id) 
                     AS t) 
ORDER BY number_of_employees_hired DESC;
		 