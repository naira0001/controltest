# main_db.py
import sqlite3
from db import queries


db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def create_db():
    if db:
        print('База данных подключена')
    cursor.execute(queries.CREATE_TABLE_store)


async def sql_insert_store(name,category, size, price,  product_id, photo):
    cursor.execute(queries.INSERT_store_query, (
        name, category, size, price, product_id, photo
    ))
    db.commit()

# CRUD - 1
# ==================================================================
def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn

def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT * FROM store """).fetchall()
    conn.close()
    return products
