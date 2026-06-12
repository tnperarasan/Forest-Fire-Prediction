import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
import pickle

from flask import Flask,render_template,request
'''
It creates an instance of the class Flask,
which will be the WSGI(Web Server Gateway Interface) Application

'''
application=Flask(__name__)
app=application

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/predictdata",methods=['GET','POST'])
def predictdata():
    if request.method=='POST':
        Temperature=request.form['Temperature']	
        RH = request.form['RH']	
        Ws=request.form['Ws']
        Rain=request.form['Rain']
        FFMC=request.form['FFMC']	
        DMC=request.form['DMC']	
        ISI=request.form['ISI']
        Classes=request.form['Classes']
        Region=request.form['Region']     
        
        ##Model Loading
        ridge_model=pickle.load(open('Notes_And_Datasets/ridge_mode.pkl','rb'))
        std_scaler=pickle.load(open('Notes_And_Datasets/scaler.pkl','rb'))  
        ## Standardizing the Data
        new_data=std_scaler.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data)
        
        return render_template('predictdata.html',results=result[0])
          
    else:
        return render_template('predictdata.html')

if __name__=='__main__':
    app.run(debug=True)
