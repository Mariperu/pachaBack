import psycopg2

def conectar_db():  
    conn = psycopg2.connect(database="hackaton06", user="postgres", password="Zal20059", host="localhost", port="5432")
    cursor = conn.cursor()

    return conn, cursor