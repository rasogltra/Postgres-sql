import os, psycopg2, sys
from dotenv import load_dotenv 

print(sys.executable)
load_dotenv() # load .env

user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_NAME")
port = os.getenv("DB_PORT")

def create_tables():
    """ create tables in the database"""

    commands = (
        """
        CREATE TABLE users (
            user_id integer PRIMARY KEY,
            username varchar(255) NOT NULL,
            email varchar(255),
            subscriber_plan varchar(255),
            region varchar(255),
            created_at timestamp
        );
        """,
        """ CREATE TABLE artists (
            artist_id integer PRIMARY KEY,
            name varchar(255),
            genre varchar(255) NOT NULL
        );
        """,
        """ CREATE TABLE albums (
            album_id integer PRIMARY KEY,
            artist_id integer REFERENCES artists (artist_id),
            title varchar(255),
            release_date timestamp  
        );
        """, 
        """ CREATE TABLE tracks (
            track_id integer PRIMARY KEY,
            album_id integer REFERENCES albums (album_id) ,
            title varchar(255),
            duration timestamp
        );
        """,
        """ CREATE TABLE listening_sessions (
                session_id integer PRIMARY KEY,
                user_id integer REFERENCES users (user_id),
                track_id integer,
                region varchar(255),
                skip_count integer,
                device_type varchar(255)  
        );      
        """,
        """ CREATE TABLE products (
                product_id integer PRIMARY KEY,
                artist_id integer REFERENCES artists (artist_id),
                type varchar(255),
                price float,
                qty integer          
            );
        """,
        """ CREATE TABLE orders (
                order_id integer PRIMARY KEY,
                user_id integer REFERENCES users (user_id),
                order_date timestamp,
                total_amount float,
                status varchar(255)      
        );
        """,
        """ CREATE TABLE order_items (
                item_id integer PRIMARY KEY,
                order_id integer,
                product_id integer REFERENCES products (product_id),
                qty integer,
                item_price float
        );
        """)
    
    conn = None
    try:
        # Establish connection
        conn = psycopg2.connect(host=host, dbname=database, user=user, password=password, port=port)
        print("Connected to pgdatabase sucessfully.")
    
        cur =conn.cursor()
    
        for command in commands:
            cur.execute(command)

        conn.commit()
        cur.close()
    
    except psycopg2.Error as error:
        print(f"Error connecting to database: {error}")
    finally:
        if conn:
            conn.close()
            print("Connection closed.")
    
if __name__ in '__main__':
    create_tables()