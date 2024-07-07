flag = []

enc = "uI2^uStUI^h4^ui2^M0Fiu^uI5u^V0mM^FT0ehOf^X1T^G1sV5sE"
for i in range(len(enc)):
    xor = ord(enc[i])^1
    flag.append(chr(xor))
   
print("".join(flag))
