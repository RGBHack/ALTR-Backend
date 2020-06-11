from flask import Flask, request, render_template, make_response, redirect, jsonify
import random
import requests
import sys
import os

app = Flask(__name__)
apikey = 'sk_97e23bfddfe545ef9335ac68a66cc161'
apiurl1 = 'https://api.improvmx.com/v3/domains/altr'
apiurl2 = '.cf/aliases'

newapiurl1 = 'https://api.improvmx.com/v3/domains/altr'
newapiurl2 = '.cf/aliases/'

curdomain = int(open('/home/rgbhack/ALTR-Backend/curdomain').read())
curnum = int(open('/home/rgbhack/ALTR-Backend/curnum').read())

@app.route('/create',methods=['POST'])
def create():
	global apikey
	global apiurl
	global curdomain
	global curnum
	if curnum == 10:
		curdomain = curdomain + 1
		with open('/home/rgbhack/ALTR-Backend/curnum', 'w') as f:
			f.write('0')
			curnum = 0
		with open('/home/rgbhack/ALTR-Backend/curdomain', 'w') as f:
			f.write(str(curdomain))
	else:
		curnum = curnum + 1
		with open('/home/rgbhack/ALTR-Backend/curnum', 'w') as f:
			f.write(str(curnum))
	if curdomain > 5:
		return jsonify({"res":4000})

	username = request.json["username"]
	newmail = request.json["youremail"]
	uid = request.json["uid"]
	ret = {}
	email = username+str(random.randrange(100000,999999))
	ret["email"] = email+"@altr"+str(curdomain)+".cf"
	r = requests.post(url=apiurl1+str(curdomain)+apiurl2,headers={'Authorization':'Basic api:'+apikey},json={"forward":newmail,"alias":email})
	with open('/home/rgbhack/ALTR-Backend/logs.txt', 'w') as f:
		print(r.json(), file=f)
	with open('/home/rgbhack/ALTR-Backend/people/'+ret["email"], 'w') as f:
		f.write(uid)
	with open('/home/rgbhack/ALTR-Backend/persons/'+uid, 'a') as f:
		f.write(ret["email"])
	with open('/home/rgbhack/ALTR-Backend/status/'+ret["email"], 'w') as f:
		f.write("on")
	ret["res"] = 0
	return jsonify(ret)

@app.route('/on',methods=['POST'])
def on():
	global apikey
	global apiurl
	email = request.json["email"]
	uid = request.json["uid"]
	youremail = request.json["youremail"]
	if not os.path.exists('/home/rgbhack/ALTR-Backend/people/'+email):
		return jsonify({"res":2000})
	true_uid = open('/home/rgbhack/ALTR-Backend/people/'+email,'r').read()
	if not true_uid == uid:
		return jsonify({"res":1000})

	alias = email.split('@')[0]
	domain1 = email.split('@altr')[1]
	domain = domain1.split('.cf')[0]
	with open('/home/rgbhack/ALTR-Backend/status/'+email,'w') as f:
		f.write("on")
	r = requests.put(url=newapiurl1+domain+newapiurl2+alias,headers={'Authorization':'Basic api:'+apikey},json={"forward":youremail},verify=False)
	return(jsonify({"res":0}))

@app.route('/off',methods=['POST'])
def off():
	global apikey
	global apiurl
	email = request.json["email"]
	uid = request.json["uid"]
	youremail = request.json["youremail"]
	if not os.path.exists('/home/rgbhack/ALTR-Backend/people/'+email):
		return jsonify({"res":2000})
	true_uid = open('/home/rgbhack/ALTR-Backend/people/'+email,'r').read()
	if not true_uid == uid:
		return jsonify({"res":1000})
	alias = email.split('@')[0]
	domain1 = email.split('@altr')[1]
	domain = domain1.split('.cf')[0]
	with open('/home/rgbhack/ALTR-Backend/status/'+email,'w') as f:
		f.write("off")
	r = requests.put(url=newapiurl1+domain+newapiurl2+alias,headers={'Authorization':'Basic api:'+apikey},json={"forward":"hi@altr.cf"},verify=False)
	with open('/home/rgbhack/ALTR-Backend/logs.txt','w') as f:
		print(newapiurl1+domain+newapiurl2+alias,file=f)
	return(jsonify({"res":0}))

@app.route('/emails',methods=['POST'])
def emails():
	uid = request.json["uid"]
	if not os.path.exists('/home/rgbhack/ALTR-Backend/persons/'+uid):
		return jsonify({"res":3000})
	with open('/home/rgbhack/ALTR-Backend/persons/'+uid, 'r') as f:
		base_lines = f.readlines()
		lines = []
		for line in base_lines:
			lines.append(line.strip())
		return(jsonify({"emails":lines,"res":0}))

@app.route('/status',methods=['POST'])
def status():
	uid = request.json["uid"]
	email = request.json["email"]
	if not os.path.exists('/home/rgbhack/ALTR-Backend/people/'+email):
		return jsonify({"res":2000})
	true_uid = open('/home/rgbhack/ALTR-Backend/people/'+email,'r').read()
	if not true_uid == uid:
		return jsonify({"res":1000})
	with open('/home/rgbhack/ALTR-Backend/status/'+email, 'r') as f:
		return jsonify({"status":f.read(),"res":0})

@app.route('/')
def index():
	return render_template('index.html')

app.run(debug=True, host='0.0.0.0', port=80)
