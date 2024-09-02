## 1. Write the SQL queries to display the total amount earned by each employee's name and surname.
```sql
SELECT 
  Emp.FirstName, 
  Emp.LastName, 
  SUM(P.ValueUSD) AS totalEarned
FROM 
  Employee Emp
JOIN 
  Payments P ON Emp.EmployeeID = P.EmployeeID
GROUP BY 
  Emp.EmployeeID;  
```
## 2. Display all employees that have their names starting with the J letter.
```sql
SELECT * FROM Employee WHERE FirstName LIKE 'J%';
```
