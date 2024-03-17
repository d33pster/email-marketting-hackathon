#!/usr/bin/env python3

import socket
import threading
import os, platform

def handleclient(connection, address):
    try:
        global addresses
        connected = True
        while connected:
            message_length = connection.recv(64).decode('utf8')
            if message_length:
                message_length = int(message_length)
                connection.send('gotint'.encode())
                message = connection.recv(message_length).decode('utf8')
                if message and message == 'disconnect':
                    connected=False
                    connection.send('disconnected')
                    break
                elif message and message!='disconnect':
                    with open('chat.bak', 'a') as chat:
                        chat.write(message+"\n")
        connection.close()
    except ConnectionResetError:
        pass

def main():
    if platform.system()=='Windows':
        os.system('cls')
    elif platform.system()=='Linux' or platform.system()=='Darwin':
        os.system('clear')
    
    print('[server running]')
    global server, addresses
    server.bind(('0.0.0.0', 8080))
    server.listen()
    while True:
        connection, address = server.accept()
        addresses.append(address)
        thread = threading.Thread(target=handleclient, args=(connection, address))
        thread.start()
        print(f'\nconnected to {address} ', f'Active: {threading.active_count()-1}')

if __name__=="__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addresses = []
    outputs = []
    try:
        main()
    except KeyboardInterrupt:
        server.close()