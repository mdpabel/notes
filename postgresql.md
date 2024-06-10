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
