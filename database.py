import psycopg2

def get_db():
    return psycopg2.connect(
        dbname="ymmo_db", 
        user="postgres", 
        password="Azerty123!", 
        host="localhost"
    )