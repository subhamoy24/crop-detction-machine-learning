from flask import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeRegressor
from predict import getPred
app=Flask(__name__)
@app.route('/')
def hello():
    return "cgbcghh"
@app.route('/pred',methods=['POST'])
def pred():
    ah=float(request.form['Air_Humidity'])
    atemp=float(request.form['Air_Temp'])
    pH=float(request.form['Soil_pH'])
    rain=float(request.form['Rainfall'])
    print(ah,atemp,pH,rain)
    l=[]
    l.append(atemp)
    l.append(ah)
    l.append(pH)
    l.append(rain)
    predictcrop=[l]
   
    #Predicting the crop
    predictions = getPred(predictcrop)
    response=jsonify({
        "predicted_crop": predictions
    })
    response.headers.add("Access-Control-Allow-Origin",'*')
    return response

if __name__=='__main__':
    app.run(debug=True)
