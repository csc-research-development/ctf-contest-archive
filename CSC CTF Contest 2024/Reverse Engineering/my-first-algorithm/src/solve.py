def reverse_scramble(input_str, shift):
    if len(input_str) != 32:
        raise ValueError("Nuh Uh")

    input_str = input_str[::-1]
    buffer = []
    temp = [0] * 32

    for i in range(16, 32):
        temp[47-i] = input_str[i]
    for i in range(12, 16):
        temp[27-i] = input_str[i]
    for i in range(11, 8, -2):
        temp[i] = input_str[i]
    for i in range(8, 12, 2):
        temp[18-i] = input_str[i]
    for i in range(7, -1, -1):
        temp[i] = input_str[i]

    for i in range(len(temp)):
        buffer.append((temp[i] - shift) % 128)
    
    return(bytes(buffer))

def xor(flag, key):
    temp = []
    for i in range(len(flag)):
        x = flag[i]
        y = key[i % len(key)]
        temp.append(x ^ y)
    return bytes(temp)

def bruteforce(ct, random_str, key):
    for word in random_str:
        curr = xor(ct, word.encode())
        curr = xor(curr, key.encode())

        for i in range(5, 14):
            pt = reverse_scramble(curr, i)
            
            if (b"CSC{" in pt):
                print(f"Found flag: {pt.decode()}")
                break

ct = b'4/jd4c?rl#z6jmw\x00kn:x}m)s5jr%\x05SS@'
random_str = ['apakah', 'kamu', 'merasa', 'ada', 'sedikit', 'keanehan', 'di', 'program', 'ini', 'kawan']
key = bytes.fromhex('6170656c').decode()

bruteforce(ct, random_str, key)