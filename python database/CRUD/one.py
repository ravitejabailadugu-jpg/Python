# Extract Data from REST API

import requests
import mysql.connector

product_resp = requests.get('https://dummyjson.com/products')
prod_data = product_resp.json()

products = prod_data["products"]


# Transform data according to MySQL Product table

beauty_products = []

for product in products:

    if product["category"] == "beauty":

        beauty_products.append((
            product["id"],
            product["title"],
            product["price"],
            product["category"],
            product["discount"]
        ))


# Load data into MySQL Product table

dbcon = None
cursor = None

try:

    dbcon = mysql.connector.connect(
        host='localhost',
        user='root',
        password='raviteja',
        database='db18'
    )

    cursor = dbcon.cursor()

    sql_st = """
        INSERT INTO product
        (p_id, prod_name, price, category, discount)
        VALUES (%s, %s, %s, %s, %s)
    """

    cursor.executemany(sql_st, beauty_products)

    dbcon.commit()

    print("Beauty products:", cursor.rowcount)
    print("Inserted successfully")


except mysql.connector.Error as err:
    print("MySQL Error:", err)

except Exception as err:
    print("Error:", err)

finally:

    if cursor is not None:
        cursor.close()

    if dbcon is not None and dbcon.is_connected():
        dbcon.close()