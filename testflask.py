from codecs import ignore_errors
from fileinput import filename
from flask import Flask, request, render_template, make_response
import json
import pandas as pd

app = Flask(__name__)


@app.route("/")
def helloworld():
    return "Hello world"

@app.route("/name")
def hellokanyarat():
    return "Hello, Kanyarat!"

##api
@app.route('/request', methods=['POST'])
def request_detail():
    
    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)
    
    print(inmessage)   
    
    json_data = json.dumps({'y': 'received!' })  #เปลี่ยนข้อมูลที่เรามีเป็น json
    return json_data
#get ส่งแบบเปิดทุกคนสามารถเห็นได้


## web app
@app.route("/home", methods=['POST','GET'])   

def home():
   
    if request.method == "POST":
        dbpd = pd.read_csv('db.csv')    #โหลดตารางที่สร้างไว้
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        
        dbpd = dbpd.append({'name': first_name,'lastname': last_name}, ignore_index = True)     
        dbpd.to_csv('db.csv', index=False)     #ignore_index คือ ตัวเลขข้างหน้า
        
        resp = make_response(render_template("home.html", name = f"{first_name} {last_name}", show =""))
        resp.set_cookie('firstname', first_name)
        
        return resp
        
        # return render_template("home.html", name = f"{first_name} {last_name}" , show ="")  
      
    if request.method == "GET":
        getval = request.args
        print(getval)   
        print(getval.get('name'))
    
    return render_template("home.html", name = 'Pond', show ="")


@app.route("/home2", methods=['POST'])
def home2():
    
    major = request.form["name_program"]
    print(major)   
    
    return render_template("home.html", name = 'Pond', show = major)
        
    
if __name__=="__main__":
    app.run()#(host='0.0.0.0')