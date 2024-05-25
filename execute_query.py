import sqlite3

def execute_query(query, params=()):
    with sqlite3.connect('university.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()
    return results

def main():
    queries = {
        "query_1": '''
            SELECT s.first_name, s.last_name, AVG(g.grade) as avg_grade
            FROM students s
            JOIN grades g ON s.student_id = g.student_id
            GROUP BY s.student_id
            ORDER BY avg_grade DESC
            LIMIT 5;
        ''',
        "query_2": '''
            SELECT s.first_name, s.last_name, AVG(g.grade) as avg_grade
            FROM students s
            JOIN grades g ON s.student_id = g.student_id
            WHERE g.subject_id = ?
            GROUP BY s.student_id
            ORDER BY avg_grade DESC
            LIMIT 1;
        ''',
        "query_3": '''
            SELECT g.group_name, AVG(gr.grade) as avg_grade
            FROM groups g
            JOIN students s ON g.group_id = s.group_id
            JOIN grades gr ON s.student_id = gr.student_id
            WHERE gr.subject_id = ?
            GROUP BY g.group_id;
        ''',
        "query_4": '''
            SELECT AVG(grade) as avg_grade
            FROM grades;
        ''',
        "query_5": '''
            SELECT sub.subject_name
            FROM subjects sub
            WHERE sub.teacher_id = ?;
        ''',
        "query_6": '''
            SELECT s.first_name, s.last_name
            FROM students s
            WHERE s.group_id = ?;
        ''',
        "query_7": '''
            SELECT s.first_name, s.last_name, g.grade
            FROM students s
            JOIN grades g ON s.student_id = g.student_id
            WHERE s.group_id = ? AND g.subject_id = ?;
        ''',
        "query_8": '''
            SELECT AVG(g.grade) as avg_grade
            FROM grades g
            JOIN subjects sub ON g.subject_id = sub.subject_id
            WHERE sub.teacher_id = ?;
        ''',
        "query_9": '''
            SELECT DISTINCT sub.subject_name
            FROM subjects sub
            JOIN grades g ON sub.subject_id = g.subject_id
            WHERE g.student_id = ?;
        ''',
        "query_10": '''
            SELECT DISTINCT sub.subject_name
            FROM subjects sub
            JOIN grades g ON sub.subject_id = g.subject_id
            WHERE g.student_id = ? AND sub.teacher_id = ?;
        '''
    }

    # Виконання кожного запиту та виведення результатів
    print("Query 1: 5 студентів із найбільшим середнім балом з усіх предметів")
    results = execute_query(queries["query_1"])
    for row in results:
        print(row)
    print("\n")

    print("Query 2: Студент із найвищим середнім балом з певного предмета (subject_id = 1)")
    results = execute_query(queries["query_2"], (1,))
    for row in results:
        print(row)
    print("\n")

    print("Query 3: Середній бал у групах з певного предмета (subject_id = 1)")
    results = execute_query(queries["query_3"], (1,))
    for row in results:
        print(row)
    print("\n")

    print("Query 4: Середній бал на потоці (по всій таблиці оцінок)")
    results = execute_query(queries["query_4"])
    for row in results:
        print(row)
    print("\n")

    print("Query 5: Які курси читає певний викладач (teacher_id = 1)")
    results = execute_query(queries["query_5"], (1,))
    for row in results:
        print(row)
    print("\n")

    print("Query 6: Список студентів у певній групі (group_id = 1)")
    results = execute_query(queries["query_6"], (1,))
    for row in results:
        print(row)
    print("\n")

    print("Query 7: Оцінки студентів у окремій групі з певного предмета (group_id = 1, subject_id = 1)")
    results = execute_query(queries["query_7"], (1, 1))
    for row in results:
        print(row)
    print("\n")

    print("Query 8: Середній бал, який ставить певний викладач зі своїх предметів (teacher_id = 1)")
    results = execute_query(queries["query_8"], (1,))
    for row in results:
        print(row)
    print("\n")

    print("Query 9: Список курсів, які відвідує студент (student_id = 1)")
    results = execute_query(queries["query_9"], (1,))
    for row in results:
        print(row)
    print("\n")

    print("Query 10: Список курсів, які певному студенту читає певний викладач (student_id = 1, teacher_id = 1)")
    results = execute_query(queries["query_10"], (1, 1))
    for row in results:
        print(row)
    print("\n")

if __name__ == "__main__":
    main()