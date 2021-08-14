DB_HOST = "ec2-34-195-143-54.compute-1.amazonaws.com"
DB_NAME = "d659nvkdfnpq6i"
DB_USER = "wsiozdazunoqwa"
DB_PASS = "efd187272cb7bc6b062316b9dd8eb1a1fe171ee4675ef01c03e7546f12a645f8"

import psycopg2
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS")

conn.close()