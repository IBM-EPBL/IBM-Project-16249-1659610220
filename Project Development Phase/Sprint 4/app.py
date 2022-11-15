
import numpy as np
from flask import Flask,render_template,request
import pickle
app= Flask(__name__)
model=pickle.load(open(r'I:\Projects\WQP\wqi.pkl','rb'))
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
  total = [[float(do),float(ph),float(co),float(bod),float(na),float(tc)]]
  y_pred = model.predict(total)
  y_pred = y_pred[[0]]
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
