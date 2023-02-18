from db_connection import connection

create_table_groups = """
CREATE TABLE IF NOT EXISTS groups_st (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  name VARCHAR UNIQUE
);
"""

create_table_teachers = """
CREATE TABLE IF NOT EXISTS teachers (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  fullname VARCHAR
);
"""

create_table_students = """
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  fullname VARCHAR,
  group_id INTEGER REFERENCES groups_st (id)
);
"""

create_table_disciplines = """
CREATE TABLE IF NOT EXISTS disciplines (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  name VARCHAR,
  teacher_id INTEGER REFERENCES teachers (id)
);
"""

create_table_grades = """
CREATE TABLE IF NOT EXISTS grades (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  discipline_id INTEGER REFERENCES disciplines (id),
  student_id INTEGER REFERENCES students (id),
  grade INTEGER,
  date_of DATE
);
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
        