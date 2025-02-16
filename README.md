# Columnar-Vs.-Row-Storage

psql -U postgres

CREATE DATABASE reviews;

#Performans Karşılaştırması

SELECT customer_id, review_date, review_rating, product_id, product_title
FROM customer_reviews_row
WHERE customer_id ='A27T7HVDXA3K2A'
  AND product_title LIKE '%Dune%'
  AND review_date BETWEEN '1998-01-01' AND '1998-12-31';


row -
Wall time: 1.79 s

colomnar -
Wall time: 197 ms

✅ OLTP işlemleri için Row-Based Storage kullanılır.
✅ OLAP ve büyük veri analizleri için Columnar Storage daha hızlıdır.
✅ Columnar Storage, veri sıkıştırması ve sorgu performansında büyük avantaj sağlar.
✅ VS Code ile PostgreSQL'e bağlanıp, Satır ve Sütun bazlı depolama test edebilirsin.