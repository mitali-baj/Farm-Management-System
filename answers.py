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
    file = open('C:/Users/prash/Desktop/NMIMS MPSTME NEW/flask/answers image/spray.jpg','rb').read()
    
    # We must encode the file to get base64 string
    file = base64.b64encode(file)
    
    # Sample data to be inserted
    args = (file,"test solution", 19)
    
    # Prepare a query
    query = 'INSERT INTO ANSWER (ans_image, ans_description, q_id) VALUES(%s, %s, %s)'
    
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