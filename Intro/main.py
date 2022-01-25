from database import db, cursor

def add_log(text, user):
    sql = ("insert into logs(text, user) values (%s, %s)")
    cursor.execute(sql, (text, user,))
    db.commit()
    log_id = cursor.lastrowid
    print("Added log {}".format(log_id))


def get_logs():
    sql = ("select * from logs order by created desc")
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        print(row)
        print(row[1]) # That's how I can print only text field.


def get_log(id):
    sql = ("select * from logs where id = %s")
    cursor.execute(sql, (id,))
    result = cursor.fetchone()

    if result:
        for row in result:
            print(row)
            # print(row[1]) # That's how I can print only text field.


def update_log(id, text):
    sql = ("update logs set text = %s where id = %s")
    cursor.execute(sql, (text, id,))
    db.commit()
    
    print("Log updated")


def delete_log(id):
    sql = ("delete from logs where id = %s")
    cursor.execute(sql, (id,))
    db.commit()

    print("Log deleted")



if __name__ == '__main__':
    pass
    # add_log("This is log one", "Iliyan")
    # add_log("This is log two", "Spasi")
    # add_log("This is log three", "Ivan")

    # get_logs()
    # get_log(2)

    # update_log(2, "This is log T-W-O")
    # delete_log(2)