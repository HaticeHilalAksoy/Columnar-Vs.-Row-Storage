import psycopg2

# PostgreSQL bağlantısı
conn = psycopg2.connect(
    dbname="reviews",
    user="student",
    password="student",
    host="127.0.0.1",
    port="5432"
)
cur = conn.cursor()

# Row-Based Table oluşturma
cur.execute("""
DROP TABLE IF EXISTS customer_reviews_row;
CREATE TABLE customer_reviews_row (
    customer_id TEXT,
    review_date DATE,
    review_rating INTEGER,
    review_votes INTEGER,
    review_helpful_votes INTEGER,
    product_id CHAR(10),
    product_title TEXT,
    product_sales_rank BIGINT,
    product_group TEXT,
    product_category TEXT,
    product_subcategory TEXT,
    similar_product_ids CHAR(10)[]
);
""")
conn.commit()
print("Row-Based Table oluşturuldu!")

# CSV dosyasından veri yükleme
cur.execute("""
COPY customer_reviews_row FROM '/tmp/customer_reviews_1998.csv' WITH CSV;
COPY customer_reviews_row FROM '/tmp/customer_reviews_1999.csv' WITH CSV;
""")
conn.commit()
print("Veri yüklendi!")

# Bağlantıyı kapat
cur.close()
conn.close()
