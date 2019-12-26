insert into employee(emp_id,emp_name,sex,title,wage,dep_id) values(101,'John','男','经理',7000,11)
delete from employee where emp_id=1443
update employee set wage=wage*1.1 where title="部门经理"
select * from employee where wage>7000 and title="部门经理"
select sex,count(*) as 雇员人数 from employee group by sex
select * from employee where wage>7000 order by wage
select sex as 性别,count(*) as 人数,average(*) as 平均工资 from employee group by sex
