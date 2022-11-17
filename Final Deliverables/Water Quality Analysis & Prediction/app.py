
import numpy as np
from flask import Flask,render_template,request
import pickle
app= Flask(__name__)
@app.route('/')
def home() :
  return render_template("web.html")
@app.route('/login',methods = ['POST'])
def login() :
  year = request.form["year"]
  do = request.form["do"]
  ph = request.form["ph"]
  co = request.form["co"]
  bod = request.form["bod"]
  tc = request.form["tc"]
  na = request.form["na"]


   #ibm start 
  import requests

  import json
  # NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
  API_KEY = "aVlUNR8qG1__zt3tfuGBWZlSvylbjxCIDOkGDJzKyVYs"
  token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
  API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
  mltoken = token_response.json()["access_token"]

  header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

  # NOTE: manually define and pass the array(s) of values to be scored in the next line
  payload_scoring = {"input_data": [{"field": [["do","ph","co","bod","tc","na"]], "values": [[do, ph, co, bod, tc, na]]}]}


  response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/67bab83c-e463-483d-a1f8-e0cc7af4faf2/predictions?version=2022-11-16', json=payload_scoring,
  headers={'Authorization': 'Bearer ' + mltoken})
  print("Scoring response")
  predict = response_scoring.json()
  pred = (predict['predictions'][0]['values'][0][0])
  y_pred=round(pred,3)

  
 

  if(y_pred >= 95 and y_pred<=100):
    return render_template("web.html",showcase = 'Excellent, The Predicted Value Is'+ str(y_pred))
  elif(y_pred >= 89 and y_pred<=94):
    return render_template("web.html",showcase = 'Very Good, The Predicted Value Is'+ str(y_pred))
  elif(y_pred >= 80 and y_pred<=88):
    return render_template("web.html",showcase = 'Good, The Predicted Value Is'+ str(y_pred))
  elif(y_pred >= 65 and y_pred<=79):
    return render_template("web.html",showcase = 'Fair, The Predicted Value Is'+ str(y_pred))
  elif(y_pred >= 45 and y_pred<=64):
    return render_template("web.html",showcase = 'Marginal, The Predicted Value Is'+ str(y_pred))
  else:
    return render_template("web.html",showcase = 'Poor, The Predicted Value Is'+ str(y_pred))


if __name__ == '__main__':
     app.run(debug = True,port=5000)
