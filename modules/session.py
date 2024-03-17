#!/usr/bin/env python3

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode

class session:
    def __init__(self):
        self._alldetails = []
        self.sessionusername = ''
        self._session = False
        
        self._kdf = PBKDF2HMAC(
            algorithm=SHA256(),
            length=32,
            salt='wikiprospects'.encode(),
            iterations=480000,
        )
        
        self._key = urlsafe_b64encode(self._kdf.derive('wikiprospects'.encode()))
        
        self.fernet = Fernet(self._key)
        
    def _register(self, name: str, username: str, password: str):
        data = {
            "Name":name,
            "username": username,
            "password":self.fernet.encrypt(password.encode())
        }
        self._alldetails.append(data)
        
        # auto login on register
        self.sessionusername = username
        self._session = True
    
    def _login(self, username: str, password: str):
        for dictionary in self._alldetails:
            if dictionary['username'] == username:
                if dictionary['password'] == self.fernet.encrypt(password.encode()):
                    # login
                    self.sessionusername = username
                    self._session = True
                    return 'allgood'
                else:
                    return 'passerror'
            else:
                return 'usernotfound'
    
    def _logout(self):
        if not self._session:
            return 'nologin'
        else:
            self._session = False
            self.sessionusername = ''
            return 'allgood'