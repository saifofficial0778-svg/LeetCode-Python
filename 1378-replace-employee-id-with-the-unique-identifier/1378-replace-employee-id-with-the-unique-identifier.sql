# Write your MySQL query statement below
SELECT EmployeeUNI.unique_id,Employees.name
FROM Employees
left join EmployeeUNI
On Employees.id=EmployeeUNI.id
