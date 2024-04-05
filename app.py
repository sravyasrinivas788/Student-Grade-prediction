from flask import Flask,render_template,request,jsonify,redirect,session,url_for
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson.objectid import ObjectId
import numpy as np;
import joblib
import pandas as pd
import os
app=Flask(__name__,template_folder='templates')
path=os.path.dirname(os.path.abspath(__file__))
model = joblib.load(os.path.join(path,'miniproject (1).pkl')) 
client=MongoClient('mongodb://localhost:27017/')
db=client['mydatabase']
collection=db['myc']
try:
    client.server_info()
    print("ok")
except Exception as e:
    print("not")
@app.route("/")
def home():
    return render_template('home.html')

@app.route('/redirect-page', methods=['POST'])
def redirect_page():
    return redirect('/register')
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        name=request.form['name']
        roll=request.form['roll']
      
        if collection.find_one({'name':name,'roll':roll}):

            error = 'Username already exists'
            return redirect('/predict')
        else:
            user = {
            'name': name,
            'roll': roll
            }
            collection.insert_one(user)
            return redirect('/login')
        
        
        
        
    return render_template('reg.html', error=None)  
#def start():
    #return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])

def login():
    if request.method == 'POST':
        name = request.form['name']
        roll = request.form['roll']
        user = collection.find_one({'name': name})
        if user is not None and user['roll']==roll :
            print("done")
            return redirect('/predict')
        else:
            error="not done"
            print("noo")
            return render_template('reg.html',error)
    return render_template('login.html')
     
#path=os.path.dirname(os.path.abspath(__file__))
#model = joblib.load(os.path.join(path,'miniproject (1).pkl'))
@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        to_predict_list=request.form.to_dict()
        try:
            prediction=preprocess(to_predict_list)
            
            return render_template('/result.html',prediction=prediction)
        except ValueError:
            return render_template('/error.html')
        pass    
       
    return render_template('index.html')
   
def preprocess(feature):
    test_data={k:[v] for k,v in feature.items()}
    test_data=pd.DataFrame(test_data)
    file=open("miniproject (1).pkl","rb")
    tarined_model=joblib.load(file)
    predict=tarined_model.predict(test_data)
    return predict
    pass
if __name__=='__main__':

    app.run(debug=True)








