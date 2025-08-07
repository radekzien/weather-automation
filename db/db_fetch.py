import psycopg2
from config import config

def fetch_subscribers():
    conn = None
    try:
        params = config()
        print("Connecting to database...")
        conn = psycopg2.connect(**params)
        print("Connection successful!")

        cur = conn.cursor()

        cur.execute("SELECT * FROM subscribers;")
        subscribers = cur.fetchall()
        for row in subscribers:
            print(row)

        return subscribers
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")
    
if __name__ == '__main__':
    fetch_subscribers()
