from flask import Flask, request, render_template

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


## web app
@app.route("/home", methods=['POST','GET'])
def home():
    
    if request.method == "POST":
        
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        
        return render_template("home.html", name = f"{first_name} {last_name}" , show ="")    
    return render_template("home.html", name = 'Pond', show ="")


@app.route("/home2", methods=['POST'])
def home2():
    
    major = request.form["name_program"]
    print(major)   
    
    return render_template("home.html", name = 'Pond', show = major)
        
    
if __name__=="__main__":
    app.run()#(host='0.0.0.0')