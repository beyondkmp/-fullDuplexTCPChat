#!/usr/bin/env python

from socket import *
from time import ctime
import select
import sys
HOST=''
PORT=21569
BUFSIZ=1024
ADDR=(HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
input=[tcpSerSock,sys.stdin]

while True:
	print 'waiting for connection...'
	tcpCliSock,addr=tcpSerSock.accept()
	print '...connected from:',addr
	input.append(tcpCliSock) #不同的就在这里，当有客户端连接时，要把他加进input

	while True:
		readyInput,readyOutput,readyException=select.select(input,[],[]) #每次循环都会阻塞在这里，只有当有数据输入时才会执行下面的操作
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
				tcpCliSock.send('[%s] %s'%(ctime(),data))

tcpCliSock.close()
