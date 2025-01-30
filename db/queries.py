# queries.py

CREATE_TABLE_store = """
   CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    size TEXT,
    price TEXT,
    product_id INTEGER ,
    photo TEXT
    )
"""



INSERT_store_query = """
    INSERT INTO store (name,category,size,price,product_id,photo)
    VALUES (?,?,?,?,?,?)
"""