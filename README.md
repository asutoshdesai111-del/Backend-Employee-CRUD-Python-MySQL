# Employee Management System

A console-based Employee CRUD application built with Python and MySQL.

## Technology

- Python 3.11.9
- MySQL 8.0.46
- mysql-connector-python 26.10.0

## Features

- Add an employee
- View all employees
- Search an employee by ID
- Update employee details
- Delete an employee with confirmation

## Project Structure

```text
.
|-- main.py
|-- config/
|   `-- db.py
|-- controller/
|   `-- employee_controller.py
|-- model/
|   `-- employeeModel.py
|-- .env.example
|-- README.md
`-- .gitignore
```

## Database Setup

Create the database and table in MySQL:

```sql
CREATE DATABASE employee_db;

USE employee_db;

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    department VARCHAR(100),
    salary FLOAT
);
```

## Configuration

Install the connector:

```powershell
python -m pip install mysql-connector-python
```

Create a `.env` file or set these environment variables:

```text
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=employee_db
```

In PowerShell, you can set variables before running:

```powershell
$env:DB_PASSWORD="your_mysql_password"
python main.py
```

The `.env` file is ignored by Git. Never commit database passwords.
