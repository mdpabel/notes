---
title: Postgresql
description: Postgresql
date: 07-06-2024
status: published
priority: 997
---

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

```sql
COPY employees (first_name, last_name, email, salary, department_id, additional_info, skills)
from '/docker_data/employees.csv'
with (format csv, delimiter ',', header);
```

## SELECTs

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

#### Using CASE with SELECT

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
