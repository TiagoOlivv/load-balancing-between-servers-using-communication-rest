import string, socket
from flask import Flask, jsonify


app = Flask(__name__)
hostname = socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 0))
port = sock.getsockname()[1]
sock.close()


@app.route('/<name>', methods=['GET','POST'])
def main(name):
	print("O que foi recebido: ", name)
	data = {
		"enviado": name,
		"resposta": name.upper(),
    }
	print("O que será enviado: ", name.upper())
	return jsonify(data)

if __name__ == '__main__':
    app.run(debug = True, host = socket.gethostbyname(hostname), port = (port))