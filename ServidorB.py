# coding: utf-8
import string, socket, psutil
from flask import Flask, jsonify


app = Flask(__name__)
hostname = socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 0))
port = sock.getsockname()[1]
sock.close() 

@app.route('/head/', methods=['HEAD','GET','POST'])
def main():
	cpu = psutil.cpu_percent(interval=1, percpu=True)
	cores = psutil.cpu_count()
	cpu = sum(cpu)/cores
	return jsonify({'CPU':cpu})

@app.route('/head/<name>', methods=['GET','POST'])
def text(name):
	data = {
		"Entrada": name,
		"Resposta": contar(name),
    }
	return jsonify(data)

def contar(str):
    counts = dict()
    words = str.split()
    
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

if __name__ == '__main__':
    app.run(debug = True, host = socket.gethostbyname(hostname), port = 40002)