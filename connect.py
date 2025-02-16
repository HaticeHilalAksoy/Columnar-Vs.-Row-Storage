import psycopg2

conn = psycopg2.connect(
    dbname="reviews",
    user="postgres",
    password="student",
    host="127.0.0.1",
    port="5432"
)
cur = conn.cursor()
print("Bağlantı başarılı!")
