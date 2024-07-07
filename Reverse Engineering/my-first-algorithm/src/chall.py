# program pertama yang aku buat dari bahasa python, masih banyak kurangnya :(
# tapi gapapa hehe yang penting masih bisa jalan :D
# coba di analisis dong program enkripsiku ini, kalau ada vulnerabilitynya kabarin aku yah >.<
# goodluck guys!!! >.<

from random import *

with open('secret-key.txt', 'rb') as rahasia:
    key = rahasia.read().hex()

print(f'key = {key}')
# key = 6170656c

flag = b'ini_bukan_flagnya_plis_jangan_di_submit'
shifter = randint(6,13)
random_str = 
['apakah', 
'kamu', 
'merasa', 
'ada', 
'sedikit', 
'keanehan', 
'di', 
'program', 
'ini', 
'kawan']

def eksklusif_atau(flag, key):
    temp = []
    
    for i in range(len(flag)):
        x = flag[i]
        y = key[i % len(key)]
        temp.append(x ^ y)

    return bytes(temp)

def telur_orak_arik_diacak_dan_dibalik(input_str, shift):
    if (len(input_str) != 32):
        raise ValueError("Nuh uh")
    
    buffer = []
    temp = [0] * 32

    for i in range(len(input_str)):
        buffer.append((input_str[i] + shift) % 128)

    for i in range(7,-1,-1):
        temp[i] = buffer[i]

    for i in range(8,12,2):
        temp[i] = buffer[18-i]

    for i in range(11,8,-2):
        temp[i] = buffer[i]

    for i in range(12,16):
        temp[i] = buffer[27-i]

    for i in range(16,32):
        temp[i] = buffer[47-i]

    return bytes(temp[::-1])

scrambled = telur_orak_arik_diacak_dan_dibalik(flag, shifter)
ctxt = eksklusif_atau(scrambled, key.encode())
ctxt = eksklusif_atau(ctxt, choice(random_str).encode())
print(f'output = {ctxt}')
# output = b'4/jd4c?rl#z6jmw\x00kn:x}m)s5jr%\x05SS@'