# Write your MySQL query statement below
SELECT name FROM employee WHERE id in (SELECT managerid from employee Group by managerID having COUNT(*) >= 5);