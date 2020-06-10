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

curdomain = int(open('/home/rgbhack/curdomain').read())
curnum = int(open('/home/rgbhack/curnum').read())

@app.route('/create',methods=['POST'])
def create():
	global apikey
	global apiurl
	global curdomain
	global curnum
	if curnum == 10:
		curdomain = curdomain + 1
		with open('/home/rgbhack/curnum', 'w') as f:
			f.write('0')
			curnum = 0
		with open('/home/rgbhack/curdomain', 'w') as f:
			f.write(str(curdomain))
	else:
		curnum = curnum + 1
		with open('/home/rgbhack/curnum', 'w') as f:
			f.write(str(curnum))

	username = request.json["username"]
	newmail = request.json["email"]
	uid = request.json["uid"]
	ret = {}
	email = username+str(random.randrange(100000,999999))
	ret["email"] = email+"@altr"+str(curdomain)+".cf"
	r = requests.post(url=apiurl1+str(curdomain)+apiurl2,headers={'Authorization':'Basic api:'+apikey},json={"forward":newmail,"alias":email})
	with open('/home/rgbhack/logs.txt', 'w') as f:
		print(r.json(), file=f)
	with open('/home/rgbhack/people/'+ret["email"], 'w') as f:
		f.write(uid)
	return jsonify(ret)

@app.route('/on',methods=['POST'])
def on():
	global apikey
	global apiurl
	email = request.json["email"]
	uid = request.json["uid"]
	youremail = request.json["youremail"]
	if not os.path.exists('/home/rgbhack/people/'+email):
		return jsonify({"ERROR","NOT AN EMAIL DUMMY"})
	true_uid = open('/home/rgbhack/people/'+email,'r').read()
	if not true_uid == uid:
		return jsonify({"ERROR","BAD UID"})

	alias = email.split('@')[0]
	domain1 = email.split('@altr')[1]
	domain = domain1.split('.cf')[0]
	r = requests.put(url=newapiurl1+domain+newapiurl2+alias,headers={'Authorization':'Basic api:'+apikey},json={"forward":youremail},verify=False)
	return({"done":"done"})

@app.route('/off',methods=['POST'])
def off():
	global apikey
	global apiurl
	email = request.json["email"]
	uid = request.json["uid"]
	youremail = request.json["youremail"]
	if not os.path.exists('/home/rgbhack/people/'+email):
		return jsonify({"ERROR":"NOT AN EMAIL DUMMY"})
	true_uid = open('/home/rgbhack/people/'+email,'r').read()
	if not true_uid == uid:
		return jsonify({"ERROR":"BAD UID"})
	alias = email.split('@')[0]
	domain1 = email.split('@altr')[1]
	domain = domain1.split('.cf')[0]
	r = requests.put(url=newapiurl1+domain+newapiurl2+alias,headers={'Authorization':'Basic api:'+apikey},json={"forward":"hi@altr.cf"},verify=False)
	with open('/home/rgbhack/logs.txt','w') as f:
		print(newapiurl1+domain+newapiurl2+alias,file=f)
	return({"done":"done"})

@app.route('/')
def index():
	return render_template('index.html')

app.run(debug=True, host='0.0.0.0', port=80)
