import csv
import random
import json
from faker import Faker
import datetime

fake = Faker()

# Number of rows
num_rows = 1_000_000

# Departments - assuming 10 departments for random distribution
department_ids = list(range(1, 11))
skills_list = ["SQL", "Java", "Python", "JavaScript", "C++", "Excel", "Management"]

# File path
csv_file_path = 'employees.csv'

# Writing to the CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["first_name", "last_name", "email", "salary", "department_id", "hire_date", "additional_info", "skills"])
    
    for _ in range(num_rows):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower()}.{last_name.lower()}@{fake.domain_name()}"
        salary = round(random.uniform(30_000, 150_000), 2)
        department_id = random.choice(department_ids)
        hire_date = fake.date_between(start_date='-5y', end_date='today')
        additional_info = json.dumps({
            "address": fake.address(),
            "phone_number": fake.phone_number()
        })
        skills = "{" + ",".join(random.sample(skills_list, random.randint(1, 4))) + "}"
        
        writer.writerow([first_name, last_name, email, salary, department_id, hire_date, additional_info, skills])

print(f'CSV file {csv_file_path} generated successfully.')
