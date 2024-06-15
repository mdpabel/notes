---
title: Postgresql
description: Postgresql
date: 07-06-2024
status: published
priority: 997
---

## Table of contents

## Setup (Docker)

1. Pull the Postgres Docker Image

```bash
docker pull postgres
```

2. Run the Postgres Docker Container

```bash
docker run --name pg -e POSTGRES_PASSWORD=pass -d -v C:\docker_data:/docker_data -p 5432:5432 postgres
```

3. Start the psql command-line interface

```bash
docker exec -u postgres -it pg psql
```

## Databases and Tables

### Creating a Database

```sql
create database company;
```

- Listing Databases: \l
- Connecting to a Database: \c company

### Dropping a database

```sql
DROP DATABASE company;
```

### Creating a Table

```sql
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    department_name VARCHAR(100) UNIQUE NOT NULL
);
```

```sql
CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,      -- Primary Key Constraint
    first_name VARCHAR(50) NOT NULL,                                   -- Not Null Constraint
    last_name VARCHAR(50) NOT NULL,                                    -- Not Null Constraint
    email VARCHAR(100) UNIQUE,                                         -- Unique Constraint
    salary NUMERIC(10, 2) CHECK (salary > 0),                          -- Check Constraint
    department_id INTEGER,                                             -- Foreign Key Column
    hire_date DATE DEFAULT CURRENT_DATE,                               -- Default Constraint
    additional_info JSONB,                                             -- JSONB type column
    skills TEXT[],                                                     -- Array type column
    CONSTRAINT fk_department FOREIGN KEY(department_id) REFERENCES departments(department_id) -- Foreign Key Constraint
);
```

### Table Constraints

Constraints enforce rules for the data in a table. Common constraints include:

1. **PRIMARY KEY:** Uniquely identifies each row in a table.
2. **FOREIGN KEY:** Ensures referential integrity between tables.
3. **UNIQUE:** Ensures all values in a column are unique.
4. **NOT NULL:**Ensures a column cannot have a NULL value.
5. **CHECK:** Ensures values in a column meet a specific condition.
6. **Default Constraint:** Assigns a default value to a column if no value is specified when a row is inserted.

### Dropping Constraints

```sql
ALTER TABLE employees
DROP CONSTRAINT fk_department;
```

### ALTER TABLE

```sql
ALTER TABLE employees
ADD CONSTRAINT fk_department
FOREIGN KEY(department_id)
REFERENCES departments(department_id);
```

```sql
ALTER TABLE test
ALTER COLUMN name SET NOT NULL;

ALTER TABLE test
ADD CONSTRAINT unique_name UNIQUE (name);
```

### Dropping a table

```sql
DROP TABLE employees;
```

## INSERT

```sql
INSERT INTO departments (department_name) VALUES
('Finance'),
('Engineering'),
('Marketing');
```

```sql
INSERT INTO employees (
    first_name, last_name, email, salary, department_id, additional_info, skills
) VALUES (
    'MD', 'Pabel', 'mdpabel@gmail.com', 65000.00,
    (SELECT department_id FROM departments WHERE department_name = 'Finance'),
    '{"hobbies": ["sports"]}', ARRAY['JavaScript', 'Angular']
)
RETURING first_name, email, department_id; -- RETURNING Clause: Immediately get the values of inserted rows.
```

### UPSERT

UPSERT, a combination of "INSERT" and "UPDATE".

**If an employee's email already exists, update the salary, department_id, and additional_info.**

```sql
INSERT INTO employees (
    first_name, last_name, email, salary, department_id, additional_info, skills
) VALUES (
    'MD', 'Pabel', 'mdpabel@gmail.com', 65000.00, 1, '{"hobbies": ["reading"]}', ARRAY['SQL', 'Python']
)
ON CONFLICT (email)
DO UPDATE SET
    salary = EXCLUDED.salary,
    department_id = EXCLUDED.department_id,
    additional_info = EXCLUDED.additional_info,
    skills = EXCLUDED.skills;
```

**If an employee’s email already exists, do nothing.**

```sql
INSERT INTO employees (
    first_name, last_name, email, salary, department_id, additional_info, skills
) VALUES (
    'MD', 'Pabel', 'mdpabel@gmail.com', 65000.00, 1, '{"hobbies": ["reading"]}', ARRAY['SQL', 'Python']
)
ON CONFLICT (email) DO NOTHING;
```

**Update only if the new salary is higher than the existing one.**

```sql
INSERT INTO employees (
    first_name, last_name, email, salary, department_id, additional_info, skills
) VALUES (
    'Alice', 'Johnson', 'alice.johnson@example.com', 75000.00, 3, '{"hobbies": ["painting"]}', ARRAY['React', 'Node.js']
)
ON CONFLICT (email)
DO UPDATE SET
    salary = GREATEST(EXCLUDED.salary, employees.salary),
    department_id = EXCLUDED.department_id,
    additional_info = EXCLUDED.additional_info,
    skills = EXCLUDED.skills;
```

Key Points

- **Conflict Target:** Specify which column(s) to check for conflicts. It must be a unique or primary key constraint.
- **EXCLUDED Keyword:** Refers to the row proposed for insertion that caused the conflict.
- **Conditional Logic:** You can apply conditional logic in the DO UPDATE clause to handle conflicts more intelligently.

### Using COPY for Bulk Inserts

```csv
employees.csv

first_name,last_name,email,salary,department_id,additional_info,skills
John,Doe,john.doe@example.com,60000,1,"{""hobbies"": [""reading""]}","{SQL,Python}"
Jane,Smith,jane.smith@example.com,75000,2,"{""hobbies"": [""music"",""hiking""]}","{Java,JavaScript}"
Alice,Johnson,alice.johnson@example.com,68000,3,"{""hobbies"": [""painting""]}","{React,Node.js}"
Charlie,Brown,charlie.brown@example.com,55000,1,"{""hobbies"": [""sports""]}","{JavaScript,Angular}"
```

[Download employees.csv](https://mega.nz/file/w6ID0QyB#WWASqQftucuHvtz1EpmEuTQqZyrJiL9_s1ZCqJI71wY)

```sql
COPY employees (first_name, last_name, email, salary, department_id, additional_info, skills)
from '/docker_data/employees.csv'
with (format csv, delimiter ',', header);
```

## SELECT

```sql
-- Employees with salary greater than 50000
SELECT * FROM employees WHERE salary > 50000;

-- Employees with a specific hobby
SELECT * FROM employees WHERE additional_info->'hobbies' @> '["sports"]';

-- quering employees hobbies
select additional_info -> 'hobbies' from employees limit 2;
select additional_info -> 'hobbies' -> 0 from employees limit 2;
select additional_info -> 'hobbies' ->> 0 from employees limit 2;

-- Employees with JavaScript skill
SELECT first_name, skills  FROM employees WHERE 'JavaScript' = ANY(skills); -- ANY and ALL are used to compare a value to a set of values: SELECT * FROM students WHERE age >= ALL (ARRAY[18, 20, 22]);
select first_name, skills from employees where skills @> '{"JavaScript"}';
select first_name, skills from employees where skills @> ARRAY['JavaScript'];

-- Employees with both JavaScript and Angular skills
SELECT * FROM employees WHERE skills @> ARRAY['JavaScript', 'Angular'];

-- Employees with first name starting with 'M'
SELECT * FROM employees WHERE first_name LIKE 'M%';

-- Case-insensitive search for first name starting with 'm'
SELECT * FROM employees WHERE first_name ILIKE 'm%';

-- Employees with salary between 40000 and 70000
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 70000;

-- Employees with salary between 40000 and 70000
SELECT * FROM employees WHERE salary BETWEEN 40000 AND 70000;

-- Employees with no department assigned
SELECT * FROM employees WHERE department_id IS NULL; -- IS: Often used with NULL or boolean expressions.

-- Employees with a salary of exactly 65000
SELECT * FROM employees WHERE salary = 65000; -- Used to compare scalar values.

-- Employees in Finance department with salary > 60000
SELECT * FROM employees WHERE department_id = (SELECT department_id FROM departments WHERE department_name = 'Finance') AND salary > 60000;

-- Employees in IT or HR department
SELECT * FROM employees WHERE department_id IN (SELECT department_id FROM departments WHERE department_name IN ('Finance', 'Marketing'));

-- Employees not earning more than 70000
SELECT * FROM employees WHERE NOT (salary > 70000);

-- Employees in specific departments
SELECT * FROM employees WHERE department_id IN (SELECT department_id FROM departments WHERE department_name IN ('Finance', 'Marketing'));

-- DISTINCT Departments
SELECT DISTINCT department_id FROM employees;

```

1. \->: Extracts a JSON object field or array element.
2. \->>: Extracts a JSON object field or array element as text
3. @>: Checks if a JSON object contains another JSON object or if a JSON array contains a specified element.
4. ||: The concatenation operator, used here to append the new element to the existing array.

### Using CASE with SELECT

```sql
-- Categorize employees based on their salary:
SELECT
    first_name,
    last_name,
    salary,
    CASE
        WHEN salary >= 80000 THEN 'High'
        WHEN salary BETWEEN 50000 AND 79999 THEN 'Medium'
        ELSE 'Low'
    END AS salary_category
FROM employees;

-- Give a 10% bonus to employees in the 'Finance' department:
SELECT
    first_name,
    last_name,
    department_id,
    salary,
    CASE
        WHEN department_id = (SELECT department_id FROM departments WHERE department_name = 'Finance')
        THEN salary * 1.10
        ELSE salary
    END AS adjusted_salary
FROM employees;
```

### Sorting Results

```sql
-- Sort by salary in descending order
SELECT * FROM employees ORDER BY salary DESC;

-- Sort by department_id and then by salary in ascending order
SELECT * FROM employees ORDER BY department_id, salary;
```

### Limiting Results

```sql
-- Get the first 5 employees by employee_id
SELECT * FROM employees ORDER BY employee_id LIMIT 5;

-- Skip the first 10 employees and return the next 5
SELECT * FROM employees ORDER BY employee_id LIMIT 5 OFFSET 10;
```

### Subqueries

#### Subqueries in SELECT

```sql
-- Employees with average department salary
SELECT first_name, last_name,
       (SELECT AVG(salary) FROM employees e2 WHERE e2.department_id = e1.department_id) AS avg_salary
FROM employees e1;
```

#### Subqueries in WHERE

```sql
-- Employees earning more than the average salary
SELECT * FROM employees WHERE salary > (SELECT AVG(salary) FROM employees);
```

#### Correlated Subqueries

```sql
-- Employees earning more than the average salary of their department
SELECT first_name, last_name
FROM employees e
WHERE salary > (SELECT AVG(salary) FROM employees WHERE department_id = e.department_id);
```

#### Scalar Subqueries

```sql
-- Employees and their department's employee count
SELECT first_name, last_name,
       (SELECT COUNT(*) FROM employees e2 WHERE e2.department_id = e1.department_id) AS dept_count
FROM employees e1;
```

## UPDATE

```sql
-- Update the salary of all employees to be 10% higher than the average salary of their department:
UPDATE employees
SET salary = salary + (SELECT AVG(salary) * 0.1 FROM employees WHERE employees.department_id = employees.department_id)
WHERE department_id IS NOT NULL
RETURNING *;
```

```sql
-- Increase salary by 10% for employees in the 'IT' department and by 5% for others:
UPDATE employees
SET salary = CASE
    WHEN department_id = (SELECT department_id FROM departments WHERE department_name = 'IT') THEN salary * 1.10
    ELSE salary * 1.05
END;
```

```sql
-- add a new hobby "cycling" for Charlie Brown in the employees table
UPDATE employees
SET additional_info = jsonb_set(additional_info, '{hobbies}', additional_info->'hobbies' || '"cycling"', true)
WHERE email = 'charlie.brown@example.com';
```

1. jsonb_set updates a specific key within the JSONB column
2. The path '{hobbies}' specifies that we are updating the hobbies array.
3. The additional_info->'hobbies' || '"cycling"' concatenates the existing hobbies with the new hobby "cycling".
4. true: A boolean flag indicating whether to create the key if it does not exist.

```sql
-- add a new skill "Docker" for Alice Johnson in the employees table
UPDATE employees
SET skills = array_append(skills, 'Docker')
WHERE email = 'alice.johnson@example.com';
```

## DELETE

```sql
DELETE FROM employees
WHERE department_id = 2
RETURNING employee_id, first_name, last_name;
```

## Referential Actions

CASCADE is used in two contexts:

1. **ON DELETE CASCADE:** Automatically deletes all child records when a parent record is deleted.
2. **ON UPDATE CASCADE:** Automatically updates all child records when a parent record is updated.

#### Drop the existing foreign key constraint:

```sql
ALTER TABLE employees
DROP CONSTRAINT fk_department;
```

#### Add the new foreign key constraint with ON DELETE CASCADE and ON UPDATE CASCADE:

```sql
ALTER TABLE employees
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id)
REFERENCES departments (department_id)
ON DELETE CASCADE
ON UPDATE CASCADE;
```

- If a department is deleted from the departments table, all employees in that department (in the employees table) are automatically deleted as well.

```sql
DELETE FROM departments WHERE department_id = 1;
```

- In this case, deleting a department sets the department_id in the employees table to NULL instead of deleting the rows.

```sql
ALTER TABLE employees
DROP CONSTRAINT fk_department;

ALTER TABLE employees
ADD CONSTRAINT fk_department
FOREIGN KEY (department_id)
REFERENCES departments (department_id)
ON DELETE SET NULL;
```

- If a department's department_id is updated in the departments table, the department_id in all related employees records is automatically updated to match the new department_id.

```sql
UPDATE departments SET department_id = 2 WHERE department_id = 1;
```

## Relationships and JOIN

### One to One

Each row in one table is linked to one and only one row in another table. The foreign key in one table (usually the child) also has a unique constraint, ensuring that each value appears only once in this column.

```sql
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE user_profiles (
    profile_id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL,
    address TEXT,
    phone VARCHAR(15),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);
```

The user_profiles table has a user_id column that references the users table. The UNIQUE constraint on user_id in user_profiles ensures a one-to-one relationship. Each user can have only one profile, and each profile is linked to only one user.

### One to Many

A single row in the parent table can be linked to multiple rows in the child table. The foreign key in the child table does not have a unique constraint, allowing multiple rows to reference the same row in the parent table.

```sql
CREATE TABLE departments (
    department_id SERIAL PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
```

### Many to Many

```sql
CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    project_name VARCHAR(100) UNIQUE NOT NULL
);
```

```sql
CREATE TABLE employee_projects (
    employee_id INTEGER,
    project_id INTEGER,
    role VARCHAR(100),
    PRIMARY KEY (employee_id, project_id),
    FOREIGN KEY (employee_id) REFERENCES employees(employee_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);
```

```sql
-- Insert into projects
INSERT INTO projects (project_name) VALUES
('Project Alpha'),
('Project Beta'),
('Project Gamma');

-- Insert into employee_projects
INSERT INTO employee_projects (employee_id, project_id, role) VALUES
((SELECT employee_id FROM employees WHERE email = 'alice.smith@example.com'), (SELECT project_id FROM projects WHERE project_name = 'Project Alpha'), 'Developer'),
((SELECT employee_id FROM employees WHERE email = 'bob.brown@example.com'), (SELECT project_id FROM projects WHERE project_name = 'Project Alpha'), 'Lead Developer'),
((SELECT employee_id FROM employees WHERE email = 'alice.smith@example.com'), (SELECT project_id FROM projects WHERE project_name = 'Project Beta'), 'Tester'),
((SELECT employee_id FROM employees WHERE email = 'charlie.johnson@example.com'), (SELECT project_id FROM projects WHERE project_name = 'Project Gamma'), 'Manager');
```

## JOIN

![join](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9d/SQL_Joins.svg/1200px-SQL_Joins.svg.png?20141123194942)

### Inner Join

Combines rows from two tables based on a condition, and returns rows where the condition is true.

```sql
-- Fetching employees and their corresponding departments.
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.department_id;
```

### Left Join (or Left Outer Join)

Returns all rows from the left table and matched rows from the right table. If no match is found, NULL is returned for columns of the right table.

```sql
-- Fetching all employees and their departments, including those without a department.
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.department_id;
```

### Right Join (or Right Outer Join)

Returns all rows from the right table and matched rows from the left table. If no match is found, NULL is returned for columns of the left table.

```sql
-- Fetching all departments and their employees, including departments without employees.
SELECT e.first_name, e.last_name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.department_id;
```

### Full Join (or Full Outer Join)

Returns rows when there is a match in one of the tables. If there is no match, NULLs are returned for non-matching rows from both tables.

### Cross Join

Returns the Cartesian product of the two tables, i.e., each row from the first table is combined with all rows from the second table.

### Self Join

A table is joined with itself. Useful for hierarchical data or when comparing rows within the same table.

### Natural Join

A type of join that automatically joins tables based on columns with the same name. Be cautious as it might not always produce the desired results.

**List all employees, their departments, and the projects they are involved in.**

```sql
SELECT e.first_name, e.last_name, d.department_name, p.project_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
JOIN employee_projects ep ON e.employee_id = ep.employee_id
JOIN projects p ON ep.project_id = p.project_id;
```

**List all employees and the projects they are working on.**

```sql
SELECT e.first_name, e.last_name, p.project_name
FROM employees e
JOIN employee_projects ep ON e.employee_id = ep.employee_id
JOIN projects p ON ep.project_id = p.project_id;
```

## Aggregation

1. COUNT():Counts the number of rows or non-NULL values.
2. SUM(): Calculates the total sum of a numeric column.
3. AVG(): Calculates the average value of a numeric column.
4. MIN(): Finds the minimum value in a column.
5. MAX(): Finds the maximum value in a column.

**In SQL, any column in the SELECT clause that is not part of an aggregate function must also be included in the GROUP BY clause.**

- **Count the Number of Employees in Each Department**

```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM departments d
LEFT JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
```

- **Total Salary by Department**

```sql
SELECT d.department_name, SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name;
```

- **Count of Projects by Employee**

```sql
SELECT e.first_name, e.last_name, COUNT(ep.project_id) AS project_count
FROM employees e
LEFT JOIN employee_projects ep ON e.employee_id = ep.employee_id
GROUP BY e.first_name, e.last_name;
```

- **Average Number of Projects per Employee**

```sql
SELECT AVG(project_count) AS average_projects_per_employee
FROM (
    SELECT COUNT(ep.project_id) AS project_count
    FROM employees e
    LEFT JOIN employee_projects ep ON e.employee_id = ep.employee_id
    GROUP BY e.employee_id
) AS project_counts;
```

- **Departments with More than 2 Employees**

```sql
SELECT d.department_name, COUNT(e.employee_id) AS employee_count
FROM departments d
JOIN employees e ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING COUNT(e.employee_id) > 2;
```

- **Total Salary by Department for Employees with Specific Skills**

```sql
SELECT d.department_name, SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
WHERE 'SQL' = ANY(e.skills)
GROUP BY d.department_name;
```

### SQL Query Execution Order

1. FROM Clause
2. JOIN Clause
3. ON Clause
4. WHERE Clause
5. GROUP BY Clause
6. HAVING Clause
7. SELECT Clause
8. ORDER BY Clause
9. LIMIT Clause

## Views

views are virtual tables that allow you to save complex queries for later use

```sql
CREATE VIEW department_salaries AS
SELECT d.department_name, SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
WHERE 'SQL' = ANY(e.skills)
GROUP BY d.department_name;
```

```sql
SELECT * FROM department_salaries;
```

### Materialized Views

Materialized views store the query results physically on disk. They improve performance by eliminating the need to re-execute complex queries every time data is accessed.

```sql
CREATE MATERIALIZED VIEW department_salaries_mv AS
SELECT d.department_name, SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e ON d.department_id = e.department_id
WHERE 'SQL' = ANY(e.skills)
GROUP BY d.department_name;
WITH NO DATA;
-- WITH DATA;
```

```sql
SELECT * FROM department_salaries_mv;
```

```sql
REFRESH MATERIALIZED VIEW department_salaries_mv;
```

**Comparing Materialized Views and Regular Views**

| Aspect             | Materialized View                           | Regular View                                             |
| ------------------ | ------------------------------------------- | -------------------------------------------------------- |
| **Storage**        | Physically stores query results.            | Stores only the query definition.                        |
| **Performance**    | Faster for complex queries, read-intensive. | Slower for complex queries, as the query runs each time. |
| **Data Freshness** | Needs manual or scheduled refresh.          | Always current (real-time).                              |
| **Use Case**       | Frequent reads, less frequent updates.      | Dynamic data where real-time results are necessary.      |
