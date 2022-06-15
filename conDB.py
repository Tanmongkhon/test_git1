import mysql.connector


def con():
    mydb = mysql.connector.connect(
    host ="localhost",
    user ="tantest",
    password ="12345",
    database ="tantest",
)
    return mydb


class Con2:
    def getHW():
        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "SELECT * FROM hard_ware"

        mycursor.execute(sql)
        
        data = mycursor.fetchall()
        mycursor.close()
        mydb.close()
        return data


    def updateStatusHW(ID, status,value):

        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE hard_ware SET status = '{}',value = {} WHERE id = {}".format(status,value, ID,)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True


    def updateusers(ID, name, last_name):

        mydb = con()

        mycursor = mydb.cursor(dictionary=True)

        sql = "UPDATE users SET name = '{}',last_name = '{}' WHERE id = {}".format(name, last_name,ID)

        mycursor.execute(sql)

        mydb.commit()

        mycursor.close()

        mydb.close()

        return True




   