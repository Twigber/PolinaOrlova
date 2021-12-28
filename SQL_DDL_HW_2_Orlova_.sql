Create table employees (
id serial primary key,
employees_name varchar (50) not null
);

insert into employees (id, employees_name)
values (default, 'Polina');


select * from employees

Create table salary (
id serial primary key,
monthly_salary int not null
);

insert into salary (id, monthly_salary)
values (default, 1000);


select * from salary

Create table employee_salary (
id serial primary key,
employee_id Int not null unique,
salary_id Int not null
);

insert into employee_salary (id, employee_id, salary_id)
values (default, 86, 20)


Create table roles (
id serial primary key,
role_name Int not null unique
);

Alter table roles 
Alter column role_name type varchar(30);

insert into roles (id, role_name)
values (default, 'Junior Python developer')


update roles set role_name = 'Junior JavaScript developer'
where id = 7

update roles set role_name = 'Middle JavaScript developer'
where id = 8

insert into roles (id, role_name)
values (default, 'Junior Manual QA engineer')



Create table roles_employee (
id serial primary key,
employee_id Int not null unique,
role_id int not null
);

insert into roles_employee (id, employee_id, role_id)
values (default, 1, 1)



select * from roles_employee 

select * from roles

select * from employee_salary

select * from employees 

select * from salary 