from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import errorcode
import base64
from PIL import Image
import io 


def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


def getImagesFromDB(id):
    # Get images from DB
    # itereate over items of blob
    # for each item, save the blob as image at folder location with .jpg extension
    try:
        cnx = mysql.connector.connect(user='mitali', password='Asdf1234#',
                                    host='localhost',
                                    database='farmers')
        print("Connecting to database")
        cursor = cnx.cursor()

        
        
        query = "select t_id,tool_image from tools where t_id="+str(id[0])
        #query1 = "select tool_image from tools"
        cursor.execute(query)
        #items = list()
        rows = cursor.fetchall()
        for row in rows:
            #print("Id = ", row[0], )
            #print("Name = ", row[1])
            image = row[1]
            fileName = row[0]
            binary_data = base64.b64decode(image)
            #print("Storing image disk \n")
            write_file(binary_data, "C:/Users/prash/Desktop/NMIMS MPSTME NEW/flask/dbms project (1)/dbms project/static/"+str(fileName)+".jpg")

        cursor.close()
        #return items
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            print("complete")

def tools_db():
    try:
        cnx = mysql.connector.connect(user='mitali', password='Asdf1234#',
                                    host='localhost',
                                    database='farmers')
        print("Connecting to database")
        cursor = cnx.cursor()


        query = "select t_id,t_name,price, t_desc from tools"
        #query1 = "select tool_image from tools"
        cursor.execute(query)
        items = list()
        rows = cursor.fetchall()
        for row in rows:
            
            items.append(row)   
            print(row)
        for row in rows:
            getImagesFromDB(row)
        cursor.close()
        return items
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            print("complete")



def fertilizer_db():
    try:
        cnx = mysql.connector.connect(user='mitali', password='Asdf1234#',
                                    host='localhost',
                                    database='farmers')
        print("Connecting to database")
        cursor = cnx.cursor()


        query = "select * from fertilizer"
        cursor.execute(query)
        items = list()
        rows = cursor.fetchall()
        for row in rows:
            items.append(row)   
            print(row)

        cursor.close()
        return items
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            print("complete")

def pesticides_db():
    try:
        cnx = mysql.connector.connect(user='mitali', password='Asdf1234#',
                                    host='localhost',
                                    database='farmers')
        print("Connecting to database")
        cursor = cnx.cursor()


        query = "select * from pesticide"
        cursor.execute(query)
        items = list()
        rows = cursor.fetchall()
        for row in rows:
            items.append(row)   
            print(row)

        cursor.close()
        return items
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            print("complete")

def policies_db():
    try:
        cnx = mysql.connector.connect(user='mitali', password='Asdf1234#',
                                    host='localhost',
                                    database='farmers')
        print("Connecting to database")
        cursor = cnx.cursor()


        query = "select * from crop_policy"
        #query1 = "select tool_image from tools"
        cursor.execute(query)
        items = list()
        rows = cursor.fetchall()
        for row in rows:
            items.append(row)   
            print(row)

        cursor.close()
        return items
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            print("complete")

def saveQuestionToDB(question,db_cropname,db_image):
    try:
        cnx = mysql.connector.connect(user='mitali', password='Asdf1234#',
                                    host='localhost',
                                    database='farmers')
        print("Connecting to database")
        cursor = cnx.cursor()


        # Open a file in binary mode
       # file = open('C:/Users/prash/Desktop/NMIMS MPSTME NEW/flask/tools image/Shovel.jpg','rb').read()
        #file = open(db_image,'rb').read()
        # We must encode the file to get base64 string
        file = base64.b64encode(db_image.read())
        
        # Sample data to be inserted
        args = (file, db_cropname, question)
        
        # Prepare a query
        query = 'INSERT INTO QUESTION(q_image,crop,q_description) VALUES(%s, %s, %s)'

        
        # Execute the query and commit the database.
        cursor.execute(query,args)
        cnx.commit()
        cursor.close()
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            print("complete")
    ## insert question into db and return
    print("TODO")


def getQuestionsFromDB():
    print("TODO")


def saveAnswer(questionId):
    print("TODO")

def getAnswers(questionId):
    print("TODO")

def getQuestImagesFromDB(id):
    # Get images from DB
    # itereate over items of blob
    # for each item, save the blob as image at folder location with .jpg extension
    try:
        cnx = mysql.connector.connect(user='mitali', password='Asdf1234#',
                                    host='localhost',
                                    database='farmers')
        print("Connecting to database")
        cursor = cnx.cursor()

        
        
        query = "select q_id,q_image from question where q_id="+str(id[0])
        #query1 = "select tool_image from tools"
        cursor.execute(query)
        #items = list()
        rows = cursor.fetchall()
        for row in rows:
            #print("Id = ", row[0], )
            #print("Name = ", row[1])
            image = row[1]
            fileName = row[0]
            binary_data = base64.b64decode(image)
            write_file(binary_data, "C:/Users/prash/Desktop/NMIMS MPSTME NEW/flask/dbms project (1)/dbms project/static/"+str(fileName)+"quest.jpg")

        cursor.close()
        #return items
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            print("complete")

def showquestions_db():
    try:
        cnx = mysql.connector.connect(user='mitali', password='Asdf1234#',
                                    host='localhost',
                                    database='farmers')
        print("Connecting to database")
        cursor = cnx.cursor()


        query = "select q_id,crop, q_description from question"
        cursor.execute(query)
        items = list()
        rows = cursor.fetchall()
        for row in rows:
            
            items.append(row)   
            print(row)
        for row in rows:
            getQuestImagesFromDB(row)
        cursor.close()
        return items
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            print("complete")

def getAnsImagesFromDB(id):
    # Get images from DB
    # itereate over items of blob
    # for each item, save the blob as image at folder location with .jpg extension
    try:
        cnx = mysql.connector.connect(user='mitali', password='Asdf1234#',
                                    host='localhost',
                                    database='farmers')
        print("Connecting to database")
        cursor = cnx.cursor()

        
        
        query = "select ans_id, ans_image from answer where q_id="+str(id)
        #query1 = "select tool_image from tools"
        cursor.execute(query)
        #items = list()
        rows = cursor.fetchall()
        for row in rows:
            #print("Id = ", row[0], )
            #print("Name = ", row[1])
            image = row[1]
            fileName = row[0]
            binary_data = base64.b64decode(image)
            write_file(binary_data, "C:/Users/prash/Desktop/NMIMS MPSTME NEW/flask/dbms project (1)/dbms project/static/"+str(fileName)+"ans.jpg")

        cursor.close()
        #return items
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            print("complete")

def showanswers_db(id):
    try:
        cnx = mysql.connector.connect(user='mitali', password='Asdf1234#',
                                    host='localhost',
                                    database='farmers')
        print("Connecting to database")
        cursor = cnx.cursor()


        query = "select ans_id,ans_description from answer where q_id ="+str(id)
        cursor.execute(query)
        items = list()
        rows = cursor.fetchall()
        for row in rows:
            
            items.append(row)   
            print(row)
        for row in rows:
            getAnsImagesFromDB(id)
        cursor.close()
        return items
    except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
            print("complete")


app = Flask(__name__)
@app.route('/app', methods=['GET', 'POST']) 
def index():
    print(request.path)
    items = list()
    templateName = 'index.html'
    if request.args.get('doAction') == 'showfertilizers':
        templateName = '/showfertilizers.html'
        items = fertilizer_db()
        print(items)    
    if request.args.get('doAction') == 'showpesticides':
        templateName = '/showpesticides.html'
        items = pesticides_db()
        print(items)     
    if request.args.get('doAction') == 'showpolicies':
        templateName = '/showpolicies.html'
        items = policies_db()
        print(items)
    if request.args.get('doAction') == 'showtools':
        templateName = '/showtools.html'
        items = tools_db()        
        print(items)
    if request.args.get('doAction') == 'saveQuestion':
        
        if request.method == 'POST':
            question = request.form.get('questionText')
            db_cropname = request.form.get('cropname')
            db_image = request.form.get('image')
            print(question)   
            print(db_cropname) 
            f = request.files['image']  
            saveQuestionToDB(question,db_cropname,f)
    if request.args.get('doAction') == 'showquestions':
        templateName = '/showquestions.html'
        items = showquestions_db()        
        print(items)
    if request.args.get('doAction') == 'showanswers':
        templateName = '/showanswers.html'
        q_id = request.args.get('qid')
        items = showanswers_db(q_id)        
        print(items)

    templateName = render_template(templateName, items=items, static_folder='/static')

     
    return templateName
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)    