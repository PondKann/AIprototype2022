from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def helloworld():
    return "Hello world"

@app.route("/name")
def hellokanyarat():
    return "Hello, Kanyarat!"

##api
@app.route('/request', method=['POST'])
def request_detail():
    
    payload = request.data.decode("utf-8")
    inmessage = json.loads(payload)
    
    print(inmessage)   
    
    json_data = json.dumps({'y': 'received!' })  #เปลี่ยนข้อมูลที่เรามีเป็น json
    return json_data


## web app
@app.route("/home")
def home():
    return render_template("home.html")

    
if __name__=="__main__":
    app.run()#(host='0.0.0.0')

