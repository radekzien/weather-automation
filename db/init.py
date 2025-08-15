import psycopg2
from config import config

def init_db():
    conn = None
    try:
        params = config('db/database.ini', 'postgresql')
        print("Connecting to database...")
        conn = psycopg2.connect(**params)
        print("Connection successful!")

        cur = conn.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) NOT NULL UNIQUE,
            name VARCHAR(20) NOT NULL,
            city VARCHAR(100) NOT NULL
        );
        """)
        print("Table 'subscribers' is ready.")

        conn.commit()

        cur.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")

if __name__ == '__main__':
    init_db()