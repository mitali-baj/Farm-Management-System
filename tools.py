from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import errorcode
import base64
from PIL import Image
import io 
try:
    cnx = mysql.connector.connect(user='mitali', password='Asdf1234#',
                                host='localhost',
                                database='farmers')
    print("Connecting to database")
    cursor = cnx.cursor()


    # Open a file in binary mode
    file = open('C:/Users/prash/Desktop/NMIMS MPSTME NEW/flask/tools image/tractor.jpg','rb').read()
    
    # We must encode the file to get base64 string
    file = base64.b64encode(file)
    
    # Sample data to be inserted
    args = ('6','TEST DATA','11000',"TEST DATA", file)
    
    # Prepare a query
    query = 'INSERT INTO TOOLS VALUES(%s, %s, %s, %s, %s)'
    
    # Execute the query and commit the database.
    cursor.execute(query,args)
    cnx.commit()
except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)