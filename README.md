# University Database Project

This project involves creating a simple SQLite database to simulate a university environment. The database includes tables for students, groups, teachers, subjects, and grades. It is populated with fake data using the Faker package. Additionally, the project includes SQL queries for retrieving specific information from the database, as well as a Python script to execute those queries.

Database Schema

The database contains the following tables:

students: Stores information about students, including student_id, first_name, last_name, and group_id.

groups: Represents student groups, with group_id and group_name.

teachers: Contains teacher details, with teacher_id, first_name, and last_name.

subjects: Stores subject details, including subject_id, subject_name, and teacher_id to indicate the teacher who teaches the subject.

grades: Records student grades, with grade_id, student_id, subject_id, grade, and date_received.

Project Files

1. create_database.py
This script creates the database university.db and populates it with fake data using the Faker library. The data includes:

30-50 students across 3 groups

5-8 subjects taught by 3-5 teachers

Each student receives 10-20 grades across all subjects

2. SQL Query Files

The following SQL queries are saved in separate .sql files:

query_1.sql: Find the top 5 students with the highest average grade across all subjects.

query_2.sql: Find the student with the highest average grade in a specific subject.

query_3.sql: Find the average grade in different groups for a specific subject.

query_4.sql: Find the overall average grade in the entire database.

query_5.sql: List the courses taught by a specific teacher.

query_6.sql: List the students in a specific group.

query_7.sql: Find the grades of students in a specific group for a specific subject.

query_8.sql: Find the average grade given by a specific teacher across all subjects they teach.

query_9.sql: List the unique courses attended by a specific student.

query_10.sql: List the courses taught by a specific teacher that a specific student attends.

3. execute_queries.py

This Python script executes the SQL queries defined above using the sqlite3 module. Each query is run, and the results are printed to the console. The queries are executed as follows:

A connection to university.db is established.

Queries are defined as strings in the script.

The execute_query() function runs the query and retrieves the results.

Results are printed to the console for each query.

Requirements

Python 3.x

SQLite3

Faker package (Install via pip install faker)

How to Use

Create and Populate the Database: Run the create_database.py script to create the SQLite database and populate it with random data.

python create_database.py

Execute SQL Queries: Run the execute_queries.py script to execute predefined SQL queries and print the results.

python execute_queries.py

Run Individual Queries: You can run individual queries by executing the .sql files in an SQLite terminal or using a Python script to execute specific queries.
