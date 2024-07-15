--https://leetcode.com/problems/second-highest-salary/

SELECT MAX(salary) AS SecondHighestSalary 
FROM Employee WHERE Employee.salary NOT IN ( SELECT MAX(salary) FROM Employee )