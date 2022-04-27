import x21139474_readfroms3
import mysql.connector
from mysql.connector import Error
from datetime import datetime

data=x21139474_readfroms3.readfroms3("AKIAX4XNGG7XBMDFDMRE","SCmBBJiBGOmFX7IRD+CtXJjwNH8soUhOotmESGD7","eu-west-1","s3-creditods-landingzone","landing-app1/seq_customer_20220417.csv")



try:
   connection = mysql.connector.connect(host='creditods.ccrwfsa7yui7.eu-west-1.rds.amazonaws.com',
                             database='creditODS',
                             user='svc28021991',
                             password='NyH58upm#')
                             #auth_plugin='caching_sha2_password')

   if connection.is_connected():
       print("Connection established with MySQL DB creditODS @",datetime.now())
       cursor = connection.cursor()
       #cursor.execute("select creditODS();")
       #record=cursor.fetchone()
       #print("You're connected to the database : ",database)
   
       cursor.execute("TRUNCATE TABLE creditODS.STG_CUSTOMER") 
       for i,row in data.iterrows():
    
            sql_insert_Query = "INSERT INTO creditODS.STG_CUSTOMER VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql_insert_Query,tuple(row))
            connection.commit()
    
       print("Total Records Inserted:",i+1)

       sql_select_Query = "select * from creditODS.STG_CUSTOMER;"
       cursor.execute(sql_select_Query)
       records = cursor.fetchall()

       print("Total record count in creditODS.STG_CUSTOMER:", cursor.rowcount)
       #print ("Printing each developer record")
   
       #for row in records:
       # print (row)

       cursor.close()
       print("Connection closed with MySQL DB CreditODS @ ",datetime.now())

except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("connection is closed")
