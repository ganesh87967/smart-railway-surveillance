from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
import os
import pickle
import pymysql
import os
from django.core.files.storage import FileSystemStorage
import io
import base64
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import smtplib

from mtcnn.mtcnn import MTCNN
import numpy as np
from PIL import Image
import cv2
from keras.models import load_model
import os
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import Normalizer
from datetime import date

global uname, scaler

#mtcnn_model = MTCNN()
#facenet_model = load_model('model/facenet_keras.h5')

#get face embedding using facenet
def get_embedding(face_pixels, facenet_model):
    face_pixels = face_pixels.astype('float32')
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    samples = np.expand_dims(face_pixels, axis=0)
    embedding = facenet_model.predict(samples)
    return embedding[0]

def extract_face(filename, mtcnn_model, required_size=(160, 160)):
    image = Image.open(filename)
    image = image.convert('RGB')
    pixels = np.asarray(image)
    results = mtcnn_model.detect_faces(pixels)
    return results, pixels

labels = []
X = []
Y = []

def getID(name):
    index = 0
    for i in range(len(labels)):
        if labels[i] == name:
            index = i
            break
    return index        
    
path = "Dataset"

for root, dirs, directory in os.walk(path):
    for j in range(len(directory)):
        name = os.path.basename(root)
        if name not in labels:
            labels.append(name)
print(labels)
X = np.load('model/X.npy')
Y = np.load('model/Y.npy')

scaler = Normalizer(norm='l2')
X = scaler.fit_transform(X)

indices = np.arange(X.shape[0])
np.random.shuffle(indices)
X = X[indices]
Y = Y[indices]

accuracy = []
precision = []
recall = [] 
fscore = []

#function to calculate all metrics
def calculateMetrics(algorithm, y_test, predict):
    global graph
    a = accuracy_score(y_test,predict)*100
    p = precision_score(y_test, predict,average='macro') * 100
    r = recall_score(y_test, predict,average='macro') * 100
    f = f1_score(y_test, predict,average='macro') * 100
    accuracy.append(float(round(a, 3)))
    precision.append(float(round(p, 3)))
    recall.append(float(round(r, 3)))
    fscore.append(float(round(f, 3)))      

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)
data = np.load("model/data.npy", allow_pickle=True)
X_train, X_test, y_train, y_test = data

svm_cls = svm.SVC()
svm_cls.fit(X_train, y_train)
predict = svm_cls.predict(X_test)
calculateMetrics("SVM", y_test, predict)

rf_cls = RandomForestClassifier()
rf_cls.fit(X_train, y_train)
predict = rf_cls.predict(X_test)
calculateMetrics("Random Forest", y_test, predict)

def ViewAlerts(request):
    if request.method == 'GET':
        global fr_api, airportList, airlineList, weatherList
        weatherList = []
        airportList = []
        airlineList = []
        cols = ['Employee Name', 'Monitoring Video', 'Monitor Date', 'Status']
        output = '<table border="1" align="center" width="100%"><tr>'
        font = '<font size="" color="black">'
        for i in range(len(cols)):
            output += "<td>"+font+cols[i]+"</font></td>"
        output += "</tr>"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'person',charset='utf8')
        with con:
            cur = con.cursor()
            cur.execute("select * FROM suspicious")
            rows = cur.fetchall()
            for row in rows:
                output += "<tr><td>"+font+row[0]+"</font></td>"
                output += "<td>"+font+row[1]+"</font></td>"
                output += "<td>"+font+row[2]+"</font></td>"
                output += "<td>"+font+row[3]+"</font></td></tr>"
        output += "</table><br/><br/><br/><br/>"          
        context= {'data':output}
        return render(request, 'AdminScreen.html', context)

def ExtractFeatures(request):
    if request.method == 'GET':
        global X_train, X_test, y_train, y_test, X
        output = "Total features extracted from each face = "+str(X.shape[1])+"<br/>"
        output += "80% Face features used to train ML algorithms = "+str(X_train.shape[0])+"<br/>"
        output += "20% Face features used to test ML algorithms = "+str(X_test.shape[0])+"<br/>"
        context= {'data': output}
        return render(request, 'AdminScreen.html', context)

def TrainModels(request):
    if request.method == 'GET':
        global accuracy, precision, recall, fscore
        output='<table border=1 align=center width=100%><tr><th><font size="" color="black">Algorithm Name</th><th><font size="" color="black">Accuracy</th>'
        output += '<th><font size="" color="black">Precision</th><th><font size="" color="black">Recall</th><th><font size="" color="black">FSCORE</th>'
        output+='</tr>'
        algorithms = ['SVM with CNN Features', 'Random Forest with CNN Features']
        for i in range(len(algorithms)):
            output += '<td><font size="" color="black">'+algorithms[i]+'</td><td><font size="" color="black">'+str(accuracy[i])+'</td><td><font size="" color="black">'+str(precision[i])+'</td>'
            output += '<td><font size="" color="black">'+str(recall[i])+'</td><td><font size="" color="black">'+str(fscore[i])+'</td></tr>'
        output+= "</table></br>"
        df = pd.DataFrame([['SVM','Accuracy',accuracy[0]],['SVM','Precision',precision[0]],['SVM','Recall',recall[0]],['SVM','FSCORE',fscore[0]],
                           ['Random Forest','Accuracy',accuracy[1]],['Random Forest','Precision',precision[1]],['Random Forest','Recall',recall[1]],['Random Forest','FSCORE',fscore[1]],
                          ],columns=['Parameters','Algorithms','Value'])
        df.pivot("Parameters", "Algorithms", "Value").plot(kind='bar', figsize=(5, 3))
        plt.title("All Algorithms Performance Graph")
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        #plt.close()
        img_b64 = base64.b64encode(buf.getvalue()).decode()
        context= {'data':output, 'img': img_b64}
        return render(request, 'AdminScreen.html', context)

def IdentifyPerson(mtcnn_model, facenet_model):
    global scaler, labels, rf_cls
    results, pixels = extract_face('PersonApp/static/test.jpg', mtcnn_model)
    img = cv2.imread('PersonApp/static/test.jpg')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    db = "No Suspicious Person Identified"
    match_score = 0
    if len(results) > 0:
        for i in range(len(results)):
            x1, y1, width, height = results[i]['box']
            x1, y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height
            face = pixels[y1:y2, x1:x2]
            image = Image.fromarray(face)
            image = image.resize((160, 160))
            image = np.asarray(image)            
            embedding = get_embedding(image, facenet_model)
            test = []
            test.append(embedding)
            test = np.asarray(test)
            test = scaler.transform(test)
            predict = rf_cls.predict_proba(test)
            max_label = rf_cls.predict(test)[0]
            max_score = np.amax(predict)
            print(max_score)
            if max_score >= 0.55:
                match_score = max_score
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(img, labels[max_label]+" Suspicious", (x1, y1 + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                db = "Suspicious Detected : "+labels[max_label]
            else:
                cv2.putText(img, 'No Suspicious Person', (x1, y1 + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return match_score, db, img    

def saveAlert(fname, result):
    global uname
    dd = str(date.today())
    db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'person',charset='utf8')
    db_cursor = db_connection.cursor()
    student_sql_query = "INSERT INTO suspicious VALUES('"+uname+"','"+fname+"','"+dd+"','"+result+"')"
    db_cursor.execute(student_sql_query)
    db_connection.commit()
    

def MonitorVideoAction(request):
    if request.method == 'POST':
        global scaler, labels, rf_cls
        status = 0
        facenet_model = load_model('model/facenet_keras.h5')
        mtcnn_model = MTCNN()                  
        myfile = request.FILES['t1'].read()
        fname = request.FILES['t1'].name
        if os.path.exists('PersonApp/static/'+fname):
            os.remove('PersonApp/static/'+fname)
        with open('PersonApp/static/'+fname, "wb") as file:
            file.write(myfile)
        file.close()
        cap = cv2.VideoCapture('PersonApp/static/'+fname)
        while True:
            ret, frame = cap.read()
            if ret == True:
                if os.path.exists('PersonApp/static/test.jpg'):
                    os.remove('PersonApp/static/test.jpg')
                cv2.imwrite('PersonApp/static/test.jpg', frame)
                match_score, result, frame = IdentifyPerson(mtcnn_model, facenet_model)
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                if match_score >= 0.55 and status == 0:
                    saveAlert(fname, result)
                    status = 1
                cv2.imshow("Monitoring Video", frame)
                key = cv2.waitKey(1)
                if key == ord('q'):
                    break
            else:
                break
        cap.release()
        cv2.destroyAllWindows()
        if status == 0:
            saveAlert(fname, "No Suspicious Person Identified")
        context= {'data':'Video Processing Completed'}
        return render(request, 'UserScreen.html', context)
    
def MonitorVideo(request):
    if request.method == 'GET':
        return render(request, 'MonitorVideo.html', {})    

def UserLogin(request):
    if request.method == 'GET':
       return render(request, 'UserLogin.html', {})

def AdminLogin(request):
    if request.method == 'GET':
       return render(request, 'AdminLogin.html', {})

def AdminLoginAction(request):
    if request.method == 'POST':
        global uname
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        if username == "admin" and password == "admin":
            context= {'data':'welcome '+username}
            return render(request, 'AdminScreen.html', context)
        else:
            context= {'data':'login failed'}
            return render(request, 'AdminLogin.html', context)      

def AddEmp(request):
    if request.method == 'GET':
       return render(request, 'AddEmp.html', {})

def index(request):
    if request.method == 'GET':
        return render(request, 'index.html', {})   

def UserLoginAction(request):
    if request.method == 'POST':
        global uname
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        index = 0
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'person',charset='utf8')
        with con:    
            cur = con.cursor()
            cur.execute("select username, password FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username and password == row[1]:
                    uname = username
                    index = 1
                    break		
        if index == 1:
            context= {'data':'welcome '+username}
            return render(request, 'UserScreen.html', context)
        else:
            context= {'data':'login failed'}
            return render(request, 'UserLogin.html', context)        
    
def AddEmpAction(request):
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        gender = request.POST.get('gender', False)
        contact = request.POST.get('contact', False)
        email = request.POST.get('email', False)
        address = request.POST.get('address', False)
        dept = request.POST.get('dept', False)
        status = "none"
        con = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'person',charset='utf8')
        with con:    
            cur = con.cursor()
            cur.execute("select username FROM register")
            rows = cur.fetchall()
            for row in rows:
                if row[0] == username:
                    status = "Username already exists"
                    break
        if status == "none":
            db_connection = pymysql.connect(host='127.0.0.1',port = 3306,user = 'root', password = 'root', database = 'person',charset='utf8')
            db_cursor = db_connection.cursor()
            student_sql_query = "INSERT INTO register VALUES('"+username+"','"+password+"','"+gender+"','"+contact+"','"+email+"','"+address+"','"+dept+"')"
            db_cursor.execute(student_sql_query)
            db_connection.commit()
            print(db_cursor.rowcount, "Record Inserted")
            if db_cursor.rowcount == 1:
                status = "New Employee details added"
        context= {'data': status}
        return render(request, 'AddEmp.html', context)

def LoadDataset(request):
    if request.method == 'GET':
        return render(request, 'LoadDataset.html', {})

def LoadDatasetAction(request):
    if request.method == 'POST':
        global X, labels
        output = "Total Criminal images found in Dataset = "+str(X.shape[0])
        output += "<br/>Different Suspicious Person available in Dataset = "+str(labels)
        output+= "</table></br></br>"
        context= {'data':output}
        return render(request, 'AdminScreen.html', context)      

