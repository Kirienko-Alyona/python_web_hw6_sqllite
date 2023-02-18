import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Найти какие курсы читает определенный преподаватель.

query_5= """
SELECT t.fullname, d.name AS teacher_desciplines
FROM disciplines d
JOIN teachers t ON t.id = d.teacher_id
WHERE t.id = 2
GROUP BY d.name
ORDER BY teacher_desciplines DESC;
"""


if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query_5)
        pprint.pprint(c.fetchall())
        c.close()