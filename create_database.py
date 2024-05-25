import sqlite3
from faker import Faker
import random
from datetime import datetime

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        group_id INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        group_id INTEGER PRIMARY KEY,
        group_name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        subject_id INTEGER PRIMARY KEY,
        subject_name TEXT,
        teacher_id INTEGER,
        FOREIGN KEY(teacher_id) REFERENCES teachers(teacher_id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS grades (
        grade_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        grade INTEGER,
        date_received DATE,
        FOREIGN KEY(student_id) REFERENCES students(student_id),
        FOREIGN KEY(subject_id) REFERENCES subjects(subject_id)
    )
    ''')

def populate_data(cursor):
    fake = Faker()

    # Вставка даних у таблицю groups
    groups = ['Group A', 'Group B', 'Group C']
    for group in groups:
        cursor.execute('INSERT INTO groups (group_name) VALUES (?)', (group,))

    # Вставка даних у таблицю teachers
    teachers = []
    for _ in range(5):
        first_name = fake.first_name()
        last_name = fake.last_name()
        cursor.execute('INSERT INTO teachers (first_name, last_name) VALUES (?, ?)', (first_name, last_name))
        teachers.append(cursor.lastrowid)

    # Вставка даних у таблицю subjects
    subjects = ['Math', 'Physics', 'Chemistry', 'Biology', 'History', 'Literature', 'Art']
    for subject in subjects:
        teacher_id = random.choice(teachers)
        cursor.execute('INSERT INTO subjects (subject_name, teacher_id) VALUES (?, ?)', (subject, teacher_id))

    # Вставка даних у таблицю students
    students = []
    for _ in range(50):
        first_name = fake.first_name()
        last_name = fake.last_name()
        group_id = random.randint(1, len(groups))
        cursor.execute('INSERT INTO students (first_name, last_name, group_id) VALUES (?, ?, ?)', (first_name, last_name, group_id))
        students.append(cursor.lastrowid)

    # Вставка даних у таблицю grades
    for student_id in students:
        for subject_id in range(1, len(subjects) + 1):
            for _ in range(random.randint(10, 20)):
                grade = random.randint(1, 100)
                date_received = fake.date_between(start_date='-1y', end_date='today')
                cursor.execute('INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)', (student_id, subject_id, grade, date_received))

if __name__ == "__main__":
    # Створення з'єднання з базою даних SQLite
    conn = sqlite3.connect('university.db')
    cursor = conn.cursor()

    # Створення таблиць
    create_tables(cursor)

    # Заповнення бази даних випадковими даними
    populate_data(cursor)

    # Збереження змін та закриття з'єднання
    conn.commit()
    conn.close()
