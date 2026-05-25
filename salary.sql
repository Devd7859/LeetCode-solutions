#employee salary higheer than manager
SELECT e.name as Employee from Employee e left join Employee f on e.managerId = f.id where e.salary > f.salary;