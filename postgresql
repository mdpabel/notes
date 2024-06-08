---
title: Postgresql
description: Postgresql
date: 07-06-2024
status: draft
priority: 997
---

## Setup (Docker)

1. Pull the Postgres Docker Image

```bash
docker pull postgres
```

2. Run the Postgres Docker Container

```bash
docker run -e POSTGRES_PASSWORD=pass --name=pg -d -p 5432:5432 postgres
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

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,      -- Primary Key Constraint
    first_name VARCHAR(50) NOT NULL,                                   -- Not Null Constraint
    last_name VARCHAR(50) NOT NULL,                                    -- Not Null Constraint
    email VARCHAR(100) UNIQUE,                                         -- Unique Constraint
    salary NUMERIC(10, 2) CHECK (salary > 0),                          -- Check Constraint
    department_id INTEGER,                                             -- Foreign Key Column
    hire_date DATE DEFAULT CURRENT_DATE,                               -- Default Constraint
    -- CONSTRAINT fk_department FOREIGN KEY(department_id) REFERENCES departments(department_id) -- Foreign Key Constraint
);
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

## INSERT

```sql
INSERT INTO employees (first_name, last_name, email, salary, department_id)
VALUES
    ('John', 'Doe', 'john.doe@example.com', 50000, 1),
    ('Jane', 'Smith', 'jane.smith@example.com', 60000, 2),
    ('Alice', 'Johnson', 'alice.johnson@example.com', 55000, 1)
RETURNING employee_id, first_name, last_name;
```
