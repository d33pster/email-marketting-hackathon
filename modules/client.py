#!/usr/bin/env python3

import socket

class client:
    def __init__(self):
        self._connectTo = ('0.0.0.0', 8080)
    
    def _connect(self, message: str):
        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._client.connect(self._connectTo)
        self._client.send(str(len(message)).encode())
        if self._client.recv(6).decode()=='gotint':
            self._client.send(message.encode())
        self._client.close()