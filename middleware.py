import requests, string, asyncio, time, socket
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)
hostname = socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 0))
port = sock.getsockname()[1]
sock.close()

@app.route('/mid/<name>', methods = ['GET','POST'])
def main(name):

    caixa =  requests.post("http://192.168.0.7:5001/%s" % (name))
    
    return jsonify({
    	"Entrada": caixa.json()['enviado'],
        "Caixa Alta":  caixa.json()['resposta'],
    })

if __name__ == '__main__':
    app.run(threaded = True, debug = True, host = socket.gethostbyname(hostname),  port = (port))