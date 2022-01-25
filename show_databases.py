import mysql.connector


if __name__ == '__main__':
    mydb = mysql.connector.connect(host="127.0.0.1", user="iliyan", passwd="11Nn1213iliyan")
    
    mycursor = mydb.cursor()

    mycursor.execute("show databases")

    for item in mycursor:
        print(item)
