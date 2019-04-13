import requests, string, asyncio, time
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)

@app.route('/mid/<name>', methods = ['GET','POST'])
def main(name):

    caixa =  requests.post("http://localhost:5001/%s" % (name))
    
    return jsonify({
    	"Entrada": caixa.json()['enviado'],
        "Caixa Alta":  caixa.json()['resposta'],
    })

if __name__ == '__main__':
    app.run(threaded = True, debug = True, host= 'localhost',  port = 4000)
