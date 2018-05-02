from flask import Flask, request, render_template
import random
app = Flask(__name__)

f = open("list.txt", "r").read().split("\n")
wordSects = {2:(2,58),3:(60,645),4:(647,2433),5:(2435,4870),6:(4872,7821),7:(7823,11014)}
	
@app.route("/")
def hello():
	name = request.args.get("name")
	pwdLen = range(8,25)
	wordLen = range(2,8)
	return render_template("index.html", pL = pwdLen, wL=wordLen)
	
@app.route("/processform")
def processForm():
	mnC, mxC = int(request.args.get("mnC")),int(request.args.get("mxC"))
	leng = random.randint(mnC,mxC)
	maxW, minW = int(request.args.get("MxL")),int(request.args.get("MnL"))
	wordLenOrder = []
	sum = 0
	while sum<leng:
		r = random.randint(minW,maxW)
		if (r+sum<leng and r+sum+minW<=leng) or r+sum==leng:
			wordLenOrder.append(r)
			sum+=r
	pas = ""
	for wordLen in wordLenOrder:
		rang = wordSects[wordLen]
		ln = random.randint(rang[0], rang[1])
		pas+= f[ln]
	return render_template("index.html", password = pas)
	
if __name__=="__main__":
	app.run(debug = True)