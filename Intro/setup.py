import mysql.connector
from mysql.connector import errorcode
from database import cursor

DB_NAME = 'acme'

TABLES = {}
TABLES['logs'] = (
        "create table `logs`("
        "`id` int(11) primary key not null auto_increment,"
        "`text` varchar(250) not null,"
        "`user` varchar(250) not null,"
        "`created` datetime not null default current_timestamp"
        ");"
    )

def create_database():
    cursor.execute("create database if not exists {}".format(DB_NAME))
    print("Database {} created".format(DB_NAME))


def create_table():
    cursor.execute("use {}".format(DB_NAME))

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print("Creating table ({})... ".format(table_name, end=""))
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Already exists")
            else:
                print(err.msg)
        else:
            print("Ready")



if __name__ == '__main__':
    create_database()
    create_table()
