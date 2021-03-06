---??????? ???? ?????????? ??? ???????? ???? ? ????, ?????? ? ??????????.
select employees.employees_name, salary.monthly_salary
from employee_salary es
join employees on es.employee_id = employees.id
join salary on es.salary_id = salary.id 

---??????? ???? ?????????? ? ??????? ?? ?????? 2000.
select employees.employees_name, salary.monthly_salary
from employee_salary es
join employees on es.employee_id = employees.id
join salary on es.salary_id = salary.id 
where monthly_salary <2000

---??????? ??? ?????????? ???????, ?? ???????? ?? ??? ?? ????????. (?? ????, ?? ?? ??????? ??? ?? ????????.)
select s.monthly_salary, e.employees_name
from employee_salary es
left outer join employees e on es.employee_id = e.id 
left outer join salary s on es.salary_id = s.id 

---??????? ??? ?????????? ???????  ?????? 2000 ?? ???????? ?? ??? ?? ????????. (?? ????, ?? ?? ??????? ??? ?? ????????.)
select s.monthly_salary, e.employees_name
from employee_salary es
left outer join employees e on es.employee_id = e.id 
left outer join salary s on es.salary_id = s.id 
where monthly_salary <2000

---????? ???? ?????????? ???? ?? ????????? ??.
select e.employees_name, s.monthly_salary
from employees e 
left outer join employee_salary es on es.employee_id  = e.id 
left outer join salary s on es.salary_id = s.id 

---??????? ???? ?????????? ? ?????????? ?? ?????????.
select e.employees_name, r.role_name
from roles_employee re 
join employees e on re.employee_id = e.id 
join roles r on re.role_id = r.id 


---??????? ????? ? ????????? ?????? Java ?????????????.
select e.employees_name, r.role_name
from roles_employee re 
join employees e on re.employee_id = e.id 
join roles r on re.role_id = r.id 
where r.role_name like '%Java %'


---??????? ????? ? ????????? ?????? Python ?????????????.
select e.employees_name, r.role_name
from roles_employee re 
join employees e on re.employee_id = e.id 
join roles r on re.role_id = r.id 
where r.role_name like '%Python%'


---??????? ????? ? ????????? ???? QA ?????????.
select e.employees_name, r.role_name
from roles_employee re 
join employees e on re.employee_id = e.id 
join roles r on re.role_id = r.id 
where r.role_name like '%QA%'


---??????? ????? ? ????????? ?????? QA ?????????.
select e.employees_name, r.role_name
from roles_employee re 
join employees e on re.employee_id = e.id 
join roles r on re.role_id = r.id 
where r.role_name like '%Manual QA%'


---??????? ????? ? ????????? ??????????????? QA
select e.employees_name, r.role_name
from roles_employee re 
join employees e on re.employee_id = e.id 
join roles r on re.role_id = r.id 
where r.role_name like '%Automation QA%'

---??????? ????? ? ???????? Junior ????????????
select e.employees_name, s.monthly_salary
from roles_employee re 
join employee_salary es on es.employee_id = re.employee_id 
join salary s on s.id = es.salary_id 
join employees e on re.employee_id = e.id 
join roles r on re.role_id = r.id 
where r.role_name like '%Junior%'

---??????? ????? ? ???????? Middle ????????????
select e.employees_name, s.monthly_salary
from roles_employee re 
join employee_salary es on es.employee_id = re.employee_id 
join salary s on s.id = es.salary_id 
join employees e on re.employee_id = e.id 
join roles r on re.role_id = r.id 
where r.role_name like '%Middle%'

---??????? ????? ? ???????? Senior ????????????
select e.employees_name, s.monthly_salary
from roles_employee re 
join employee_salary es on es.employee_id = re.employee_id 
join salary s on s.id = es.salary_id 
join employees e on re.employee_id = e.id 
join roles r on re.role_id = r.id 
where r.role_name like '%Senior%'

---??????? ???????? Java ?????????????
select  r.role_name, s.monthly_salary
from roles_employee re
join employee_salary es on es.employee_id = re.employee_id 
join salary s on es.salary_id = s.id 
join employees e on re.employee_id = e.id 
join roles r on re.role_id  = r.id
where role_name like '%Java %'

---??????? ???????? Python ?????????????
select r.role_name, s.monthly_salary
from roles_employee re 
join employee_salary es on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join employees e on es.employee_id = e.id 
join roles r on re.role_id = r.id 
where role_name like '%Python%'

---??????? ????? ? ???????? Junior Python ?????????????
select r.role_name, s.monthly_salary
from roles_employee re 
join employee_salary es on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where role_name like '%Junior Python%'

---??????? ????? ? ???????? Middle JS ?????????????
select r.role_name, s.monthly_salary
from roles_employee re 
join employee_salary es on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where role_name like '%Middle JavaScript%'

---??????? ????? ? ???????? Senior Java ?????????????
select r.role_name, s.monthly_salary
from roles_employee re 
join employee_salary es on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where role_name like '%Senior Java %'

---??????? ???????? Junior QA ?????????
select r.role_name, s.monthly_salary
from roles_employee re 
join employee_salary es on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where role_name like '%Junior%' and role_name like '%QA%'

---??????? ??????? ???????? ???? Junior ????????????
select AVG(s.monthly_salary)
from employee_salary es 
join roles_employee re on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where role_name like '%Junior%'

---??????? ????? ??????? JS ?????????????
select SuM(s.monthly_salary)
from employee_salary es 
join roles_employee re on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where role_name like '%JavaScript%'

---??????? ??????????? ?? QA ?????????
select MIN(s.monthly_salary)
from employee_salary es 
join roles_employee re on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where role_name like '%QA%'


---??????? ???????????? ?? QA ?????????
select Max(s.monthly_salary)
from employee_salary es 
join roles_employee re on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where role_name like '%QA%'

---??????? ?????????? QA ?????????
select  count(r.role_name) from roles r
where role_name like '%QA%'

---??????? ?????????? Middle ????????????.
select  count(r.role_name) from roles r
where role_name like '%Middle%'

---??????? ?????????? ?????????????
select  count(r.role_name) from roles r
where role_name like '%developer%'

---??????? ???? (?????) ???????? ?????????????.
select SuM(s.monthly_salary)
from employee_salary es 
join roles_employee re on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where role_name like '%developer%'

---??????? ?????, ????????? ? ?? ???? ???????????? ?? ???????????
select e.employees_name, r.role_name, s.monthly_salary
from employee_salary es 
join roles_employee re on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
Order by monthly_salary asc

---??????? ?????, ????????? ? ?? ???? ???????????? ?? ??????????? 
---? ???????????? ? ??????? ?? ?? 1700 ?? 2300
select e.employees_name, r.role_name, s.monthly_salary
from employee_salary es 
join roles_employee re on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where monthly_salary > 1700 and monthly_salary <2300 Order by monthly_salary asc

---??????? ?????, ????????? ? ?? ???? ???????????? ?? ??????????? 
---? ???????????? ? ??????? ?? ?????? 2300
select e.employees_name, r.role_name, s.monthly_salary
from employee_salary es 
join roles_employee re on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where monthly_salary <2300 Order by monthly_salary asc

---??????? ?????, ????????? ? ?? ???? ???????????? ?? ??????????? ? ???????????? 
---? ??????? ?? ????? 1100, 1500, 2000
select e.employees_name, r.role_name, s.monthly_salary
from employee_salary es 
join roles_employee re on re.employee_id = es.employee_id 
join salary s on es.salary_id = s.id 
join roles r on re.role_id = r.id 
join employees e on re.employee_id = e.id 
where monthly_salary =1100 or monthly_salary =1500 or monthly_salary =2000 Order by monthly_salary asc