from db_connection import connection


create_table_groups = """
DROP TABLE IF EXISTS groups_st;
"""

create_table_teachers = """
DROP TABLE IF EXISTS teachers;
"""

create_table_students = """
DROP TABLE IF EXISTS students;
"""

create_table_disciplines = """
DROP TABLE IF EXISTS disciplines;
"""

create_table_grades = """
DROP TABLE IF EXISTS grades;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(create_table_teachers)
        c.execute(create_table_groups)
        c.execute(create_table_students)
        c.execute(create_table_disciplines)
        c.execute(create_table_grades)
        c.close()
        