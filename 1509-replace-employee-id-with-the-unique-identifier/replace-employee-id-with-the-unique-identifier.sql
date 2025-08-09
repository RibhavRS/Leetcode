# Write your MySQL query statement below
Select i.unique_id,e.name from Employees e
LEFT JOIN  EmployeeUNI i ON e.id = i.id