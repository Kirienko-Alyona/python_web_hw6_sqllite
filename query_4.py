import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Найти средний балл на потоке (по всей таблице оценок).

query = """
SELECT g.grade, ROUND(AVG(g.grade), 2) AS average_grade
FROM grades g
JOIN grades g ON g.id = g.grade_id
GROUP BY g.name
ORDER BY average_grade DESC;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()