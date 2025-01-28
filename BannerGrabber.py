#!/usr/bin/python3

import socket

# s = socket.socket()

# ip = input("Please enter the IP: ")
# port = str(input("Please enter the port: "))
    
# s.connect((ip, int(port)))
# print(s.recv(1024))


def banner(ip, port):
    s = socket.socket()
    s.connect((ip, int(port)))
    s.settimeout(5)
    print(s.recv(1024))
    
def main():
    ip = input("Please enter the IP: ")
    port = str(input("Please enter the port: "))
    banner(ip, port)

main()