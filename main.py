import os
import socket
from title import title
from colorama import Fore

print(Fore.BLUE+title+Fore.RESET)


def TCP_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    while True:
        try:
            host = input(Fore.CYAN+"[?] Enter a tcp server host: "+Fore.RESET)
            port = int(input(Fore.CYAN+"[?] Enter a tcp server port: "+Fore.RESET))
        except:
            print(Fore.LIGHTRED_EX+"[Er] A port must be number."+Fore.RESET)
        
        try:    
            client.connect((host, port))
        except:
            print(Fore.LIGHTRED_EX+"[Er] Invalid host or network error"+Fore.RESET)
        
        finally:
            os.system("cls")
            break

    while True:
        data = client.recv(1024).decode("utf-8")
        print(Fore.LIGHTGREEN_EX+"[TCP] data: "+Fore.RESET+f"{data}")



def UDP_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            host = input(Fore.CYAN+"[?] Enter a udp server host: "+Fore.RESET)
            port = int(input(Fore.CYAN+"[?] Enter a udp server port: "+Fore.RESET))
        except:
            print(Fore.LIGHTRED_EX+"[Er] A port must be number."+Fore.RESET)
        
        try:    
            client.connect((host, port))
        except:
            print(Fore.LIGHTRED_EX+"[Er] Invalid host or network error"+Fore.RESET)
        
        finally:
            os.system("cls")
            break

    while True:
        data = client.recv(1024).decode("utf-8")

        if data != None:
            print(Fore.LIGHTGREEN_EX+"[UDP] data: "+Fore.RESET+f"{data}")
        



while True:
    change_protocol = input(Fore.CYAN+"[?] TCP(1) or UDP(2) server:"+Fore.RESET)

    if change_protocol == "1":
        TCP_client()
    
    elif change_protocol == "2":
        UDP_client()

    else:
        print(Fore.LIGHTRED_EX+"[Er] Enter 1 if you need TCP protocol, 2 if UDP!"+Fore.RESET)
