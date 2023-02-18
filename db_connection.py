from contextlib import contextmanager
import sqlite3


@contextmanager
def connection():
    conn = None
    try:
        conn = sqlite3.connect('hw_6.db')
        yield conn
        conn.commit()
    except sqlite3.Error as error:
        print(error)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()