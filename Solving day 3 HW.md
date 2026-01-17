[[Day 3 Homework]]
![[Pasted image 20250706180356.png]]

--------------------------------------------------------------------------------------------------------

First we will open our ==TERMINAL== (We have used WARP Terminal)
and start our MYSQL Service:
```
sudo systemctl start mysql
```
We will be using the SQLECTRON app to use the MYSQL Service
![[Pasted image 20250707142400.png]]

-----------------------------------------------

We have created a Database called ==**day3subbu**==
- create database day3subbu;
next query to solve is to create a ==emp== table
- i)emp_id - Primary key
- ii)first_name - not null
- iii)last_name - not null
- iv)salary - int (not null)
- v)dept_name - varchar(255) not null
- vi)manager_name -  varchar(255) not null
```
use day3subbu;
create table emp(
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    salary INT CHECK (salary >= 0),
    dept_name VARCHAR(255) NOT NULL,
	manager VARCHAR(255)
);
desc emp;
select * from emp;
```
**And i added a constraint of ==CHECK (salary <= 0)== so that no negative or 0 is entered into the salary**
==below is our output:==
![[Pasted image 20250707143615.png]]
- Now we are required to fill in atleast 5 member details which done in the format of :
```
USE day3subbu;

INSERT INTO emp(emp_id, first_name, last_name, salary, dept_name, manager) VALUES
(101, 'Krishna', 'P', 80000, 'AI-Banking', 'Anil'),
(102, 'Sita', 'Sharma', 60000, 'Marketing', 'Priya Desai'),
(103, 'Amit', 'Verma', 45000, 'Sales', 'Rajiv Nair'),
(104, 'Neha', 'Reddy', 70000, 'HR', 'Sunita Rao'),
(105, 'Vikram', 'Patel', 55000, 'Finance', 'Amit Shah');
DESC emp;
SELECT * FROM emp;

```

--------------------------
- ==Added the details into the table successfully ==
![[Pasted image 20250707144334.png]]
--------

  
