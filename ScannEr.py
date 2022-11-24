#!/bin/python3

import socket
#socket.setdefaulttimeout(2)
from termcolor import colored


class scan:
    def portscanner(port):
        if sock.connect_ex((host, port)):
            print(colored("Port {} is Close".format(port),'red'))
        else:
            print(colored("Port {} is Open".format(port),'blue'))

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("[*]--Enter the IP Address to Scan: ")

num = int(input("""[*]--Do you want to Scan 1 port or Ranges of port: Example 1 -100
    1 = one port
    2 = ranges of port:  """))
if num==1:
    print("---------------------------------------------------------------------------------------------------")
    port = int(input("[*]--Enter the one port you want to SCAN: "))
    scan.portscanner(port)

elif num==2:
    print("---------------------------------------------------------------------------------------------------")
    F = int(input("[*]--Enter the First port of the Range you want to scan: "))
    L = int(input("[*]--Enter the Last port of the Range you want to scan: "))
    for port in range(F, (L+1)):
        scan.portscanner(port)
    



