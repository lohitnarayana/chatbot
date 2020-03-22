import nltk
import random
import string
from flask import Flask, render_template, request
from decimal import Decimal

app = Flask(__name__)
c=0
def gcd(a,b): 
    if b==0: 
        return a 
    else: 
        return gcd(b,a%b) 
def rsae(e,text,n):
    al={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    dl={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
    encri=[]
    text = nltk.word_tokenize(text)
    for i in text:
        i=list(i)
        encri_word=[]
        decri_word=[]
        for no in i:
            ctt = Decimal(0) 
            ctt =pow(al[no],e) 
            ct = ctt % n 
            encri_word.append(dl[ct%26])
        encri.append(''.join(encri_word))
    return(' '.join(encri))
def rsad(d,text,n):
    al={'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    dl={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
    decri=[]
        
    text = nltk.word_tokenize(text)
    for i in text:
        i=list(i)
        encri_word=[]
        decri_word=[]
        for no in i:
            dtt = Decimal(0)
            dtt = pow(al[no],d) 
            dt = dtt % n
            decri_word.append(dl[dt])
        decri.append(''.join(decri_word))
    return(' '.join(decri))
def response(user_response):
    word_tokens = nltk.word_tokenize(user_response)
    l=[]
    for word in word_tokens:
        if(word=='encrypt' or word == 'encryption'):
            greet = 'enter your prime number and text in the following format { rsaen prime 1 prime 2 text }'
            return greet
        elif(word=='decrypt' or word == 'decryption'):
            greet = 'enter your prime number and text in the following format{ rsadn prime 1 prime 2 text }'
            return greet
        elif(word == 'rsaen'):
            p,q = word_tokens[1],word_tokens[2]
            
            n = int(p)*int(q)
            t = (int(p)-1)*(int(q)-1)
            
            for e in range(2,t):
                if gcd(e,t)== 1: 
                    break
            for i in range(1,10): 
                x = 1 + i*t 
                if x % e == 0: 
                    d = int(x/e) 
                    break
            for i in range(3,len(word_tokens)):
                l.append(word_tokens[i])
            text = ' '.join(l)
            return rsae(e,text,n)
        elif(word == 'rsadn'):
            p,q = word_tokens[1],word_tokens[2]
            n = int(p)*int(q) 
            t = (int(p)-1)*(int(q)-1)
            encri=[]
            decri=[]
            for e in range(2,t):
                if gcd(e,t)== 1: 
                    break
            for i in range(1,10): 
                x = 1 + i*t 
                if x % e == 0: 
                    d = int(x/e) 
                    break
            for i in range(3,len(word_tokens)):
                l.append(word_tokens[i])
            text = ' '.join(l)
            return rsad(d,text,n)

def sorry():
    so = "sorry i didn't understand "
    return so    


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    if(response(userText)!=None):
        return str(response(userText))
    else:
        
        return str(sorry())



if __name__ == "__main__":
    app.run()