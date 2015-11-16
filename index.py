from flask import Flask, render_template, request, redirect
import os
from pymongo import MongoClient
app = Flask(__name__)
def connect():
# Substitute the 5 pieces of information you got when creating
# the Mongo DB Database (underlined in red in the screenshots)
# Obviously, do not store your password as plaintext in practice
    print "start connection"
    try:
        connection = MongoClient("mongodb://ds043262.mongolab.com:43262")
        handle = connection["code101"]
        handle.authenticate("admin010101","010101admin")
    except Exception as e:
        print app
        print e.args      # arguments stored in .args
        print " - init exception value: ", e
        handle = None
    return handle


handle = connection()
#handle = MongoClient('mongodb://admin010101:010101admin@ds043262.mongolab.com:43262/code101')

# Bind our index page to both www.domain.com/ and www.domain.com/index
@app.route("/index" ,methods=['GET'])
@app.route("/", methods=['GET'])
def index():
    print "hello-flask-again"
    try:
        userinputs = [x for x in handle.mycollection.find()]
    except Exception as e:
        print app
        print e.args      # arguments stored in .args
        print " - init exception value: ", e
        userinputs = None
    return render_template('index.html', userinputs=userinputs)


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
