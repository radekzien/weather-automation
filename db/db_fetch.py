import psycopg2
from config import config

params = config('db/database.ini', 'postgresql')

def fetch_subscribers():
    conn = None
    try:
        print("Connecting to database...")
        conn = psycopg2.connect(**params)
        print("Connection successful!")

        cur = conn.cursor()

        cur.execute("SELECT * FROM subscribers;")
        subscribers = cur.fetchall()
        
        for row in subscribers: #for testing
            print(row)

        return subscribers
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")

def fetch_locations():
    conn = None
    try:
        print("Connecting to database...")
        conn = psycopg2.connect(**params)
        print("Connection successful!")

        cur = conn.cursor()

        cur.execute("SELECT DISTINCT city FROM subscribers;")
        cities = cur.fetchall()

        cities = [city[0] for city in cities]

        for city in cities: #for testing
            print(city)

        return cities
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")
    
    
if __name__ == '__main__':
    fetch_subscribers()
    fetch_locations()

