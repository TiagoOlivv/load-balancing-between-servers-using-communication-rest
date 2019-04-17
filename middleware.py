# coding: utf-8
import requests, string, asyncio, time, socket, os, psutil
from flask import Flask, jsonify
from threading import Thread

app = Flask(__name__)
hostname = socket.gethostname()

@app.route('/head/<name>', methods = ['GET','POST'])
def main(name):

	ip = On()	

	if ip == 0:
		return jsonify("NAO HA SERVIDOR ONLINE NO MOMENTO")
	
	else:
		caixa =  requests.post(ip + "%s" % (name))

		return jsonify({
			"Entrada": caixa.json()['Entrada'],
			"Resposta":  caixa.json()['Resposta'],
		})

def On():
	with open('IPs.txt') as file:
		dump = file.read()
		dump = dump.splitlines()
		contServer = 0
		cpuUse = []

		for ip in dump:
			print('Requisitando em :', ip)
			
			try:
				url = str(ip)
				r = requests.head(ip)

				if r.status_code == 200 :
					print("Servidor Disponivel")
					contServer = contServer + 1
					cpu = requests.get(ip)
					alive = ip                      
					print(cpu.json())
					cpuUse.append(cpu.json()['CPU'])

			except:
				print("Servidor Indisponivel")

		print("Quantidade de Servidores Disponiveis: ", contServer)
		
		if contServer == 1:
			print("Apenas Servidor " + alive + " Online")
			return alive
		
		elif contServer == 2:
			
			if cpuUse[0] < cpuUse[1]:
				print("CPU 1 " + str(cpuUse[0]) + "\té menor que\tCPU 2 "+ str(cpuUse[1]) +"\n")
				return dump[0]
			else:
				print("CPU 1 " + str(cpuUse[0]) + "\té maior que\tCPU 2 "+ str(cpuUse[1]) +"\n")
				return dump[1]

		else:
			print ("Não existem servidores disponiveis")
			return 0

if __name__ == '__main__':
	app.run(debug = True, host = socket.gethostbyname(hostname),  port = 40000)