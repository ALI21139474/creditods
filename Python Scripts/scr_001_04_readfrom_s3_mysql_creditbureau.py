#######################################################################################################################################################
# Script Name: scr_001_04_readfrom_s3_mysql_creditbureau.py                                                                                           #
# Author: Kamrun Nahar Ali                                                                                                                            #
# Created Date: 22-04-2022                                                                                                                            #
# Parameters Required: 0                                                                                                                              #
# Script Execution Syntax: sudo python3 scr_001_04_readfrom_s3_mysql_creditbureau.py                                                                  #
#                                                                                                                                                     #
# Functionality of the script: This python script reads bureau data from Amazon S3 lake and dump data into Amazon RDS- MySql Database. This script   #
#                              imports system defined library such as mysql connector and datetime feature. It also imports user defined library that #
#                              provides module to read data from s3 lake by providing api access key,region, bucket name and file name.               #
#######################################################################################################################################################

#import library to reuse user and system defined modules
from py_proj_pkg.x21139474_readfroms3 import readfroms3
import mysql.connector
from mysql.connector import Error
from datetime import datetime
#using readfroms3 module from user defined python library py_proj_pkg.x21139474_readfroms3

data=readfroms3("AKIAX4XNGG7XBMDFDMRE","SCmBBJiBGOmFX7IRD+CtXJjwNH8soUhOotmESGD7","eu-west-1","s3-creditods-landingzone","landing-app1/seq_bureaudata_20220417.csv")


#exception handling block for making connection to AWS RDS DB-MySQL

try:
   #connect to mysql db

   connection = mysql.connector.connect(host='creditods.ccrwfsa7yui7.eu-west-1.rds.amazonaws.com',
                             database='creditODS',
                             user='svc28021991',
                             password='NyH58upm#')
                             #auth_plugin='caching_sha2_password')

   if connection.is_connected():
       print("Connection established with MySQL DB creditODS @",datetime.now())
       cursor = connection.cursor()
       #truncate table before inserting values from s3 into stage table 
       cursor.execute("TRUNCATE TABLE creditODS.STG_BUREAU_DEBT_SUMMARY") 
       #read data from s3 row by row and insert into staging table
       for i,row in data.iterrows():
    
            sql_insert_Query = "INSERT INTO creditODS.STG_BUREAU_DEBT_SUMMARY VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql_insert_Query,tuple(row))
            connection.commit()
    
       print("Total Records Inserted:",i+1)

       sql_select_Query = "select * from creditODS.STG_BUREAU_DEBT_SUMMARY;"
       cursor.execute(sql_select_Query)
       records = cursor.fetchall()

       print("Total record count in creditODS.STG_BUREAU_DEBT_SUMMARY:", cursor.rowcount)

       cursor.close()

except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    #closing database connection.
    if(connection.is_connected()):
        cursor.close()
        connection.close()
        print("Connection closed with MySQL DB CreditODS @ ",datetime.now())
