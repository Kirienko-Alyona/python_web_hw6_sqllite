import pprint

from faker import Faker

from db_connection import connection

fake = Faker('uk-UA')

#Оценки студентов в определенной группе по определенному предмету на последнем занятии.

queryold= """
SELECT s.fullname, g.name, d.name, gr.grade AS grades_students
FROM grades gr
JOIN disciplines d ON d.id = gr.discipline_id
JOIN students s ON s.id = gr.student_id
JOIN groups_st g ON g.id = s.group_id
WHERE g.id = 3 AND gr.date_of IN (
    SELECT gr.date_of 
    from grades as gr
    JOIN students s ON s.id = gr.student_id
    JOIN groups_st g ON g.id = s.group_id
    where g.id = 3 and discipline_id = 2
    order by gr.date_of desc 
    limit 1)
ORDER BY grades_students;
"""
query= """

SELECT s.fullname, g.name, d.name, gr.grade AS grades_students, gr.date_of
FROM grades gr
JOIN disciplines d ON d.id = gr.discipline_id
JOIN students s ON s.id = gr.student_id
JOIN groups_st g ON g.id = s.group_id
WHERE g.id = 3 and d.id=2 
ORDER BY gr.date_of DESC;
"""



if __name__ == '__main__':
    with connection() as conn:
        c = conn.cursor()
        c.execute(query)
        pprint.pprint(c.fetchall())
        c.close()