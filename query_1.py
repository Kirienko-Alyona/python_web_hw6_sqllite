from random import randint
import pprint

from faker import Faker

from seeds import connect

fake = Faker('uk-UA')
query_1 = """
    SELECT s.fullname, ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    GROUP BY s.fullname
    ORDER BY average_grade DESC
    LIMIT 5;
"""


if __name__ == '__main__':
    with connect() as conn:
        c = conn.cursor()
        # c.execute(simple_select, (10,))
        # print(c.fetchone())
        c.execute(query_1)
        pprint.pprint(c.fetchall())
        c.close()