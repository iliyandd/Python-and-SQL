import mysql.connector

config = {
    'user': 'iliyan',
    'passwd': '11Nn1213iliyan',
    'host': 'localhost',
    'database': 'acme'
}

db = mysql.connector.connect(**config)
cursor = db.cursor()
