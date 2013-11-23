#!/usr/bin/env python
#coding: utf-8
from socket import *
from time import ctime
import select
import sys
HOST='172.16.45.135'
PORT=21569
BUFSIZ=1024
ADDR=(HOST,PORT)  #服务器的地址与端口

tcpCliSock=socket(AF_INET,SOCK_STREAM) #生成客户端的套接字，并连上服务器
tcpCliSock.connect(ADDR)
input1=[tcpCliSock,sys.stdin]

while True:
	readyInput,readyOutput,readyException=select.select(input1,[],[])
	for indata in readyInput:
		if indata==tcpCliSock:
			data=tcpCliSock.recv(BUFSIZ)
			if not data:
				break
			print data
		else:
			data=raw_input()
			if not data:
				break
			tcpCliSock.send('[%s] %s' %(ctime(),data)) #发送时间与数据

tcpCliSock.close()
