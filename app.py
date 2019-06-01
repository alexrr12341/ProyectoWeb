from flask import Flask, redirect, render_template, request, session, url_for,abort
import requests
import os
app = Flask(__name__)
app.secret_key=str(os.system('openssl rand -base64 24'))
port=os.environ["PORT"]
@app.route('/',methods=['POST','GET'])
def inicio():
    return render_template('index.html')
@app.route('/playnow',methods=['POST','GET'])
def playnow():
    return render_template('playnow.html')
@app.route('/updates',methods=['POST','GET'])
def updates():
    return render_template('updates.html')
@app.route('/donations')
def purchase():
	try:
		return render_template("subscribe.html")
	except:
		return(str(e))
@app.route('/success')
def success():
	try:
		return render_template("success.html")
	except:
		return(str(e))
if __name__ == '__main__':
    port=os.environ["PORT"]
app.run(debug=True)