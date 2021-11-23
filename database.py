import mysql.connector

config = {
    'user': 'root',
    'password': '121212aa',
    'host': 'localhost',
    'database': 'acme',
}

db = mysql.connector.connect(**config)
cursor = db.cursor()