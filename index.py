from flask import Flask, render_template, request, redirect
import os
from pymongo import MongoClient

def connect():
# Substitute the 5 pieces of information you got when creating
# the Mongo DB Database (underlined in red in the screenshots)
# Obviously, do not store your password as plaintext in practice
    connection = MongoClient("ds043262.mongolab.com",43262)
    handle = connection["code101"]
    handle.authenticate("admin010101","010101admin")
    return handle

app = Flask(__name__)
handle = MongoClient('mongodb://admin010101:010101admin@ds043262.mongolab.com:43262/code101')

# Bind our index page to both www.domain.com/ and www.domain.com/index
@app.route("/index" ,methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    userinputs = [x for x in handle.mycollection.find()]
    return render_template('index.html', userinputs=userinputs)
#    print "hello-flask-again"

@app.route("/write", methods=['POST'])
def write():
    userinput = request.form.get("userinput")
    oid = handle.mycollection.insert({"message":userinput})
    return redirect ("/")

@app.route("/deleteall", methods=['GET'])
def deleteall():
    handle.mycollection.remove()
    return redirect ("/")

# Remove the "debug=True" for production
#if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    #port = int(os.environ.get('PORT', 5000))
    #app.run(host='0.0.0.0', port=port)
#    app.run()
