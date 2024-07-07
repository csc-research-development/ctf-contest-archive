from pwn import *
import re

def tetration_answer(x, n):
    if n == 0:
        return 1
    return x**tetration_answer(x, n - 1)

def caesar_cipher(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            ciphertext += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            ciphertext += char
    return ciphertext

def vigenere_cipher(plaintext, key):
    ciphertext = ""
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shift = ord(key[i % key_length].lower()) - ord('a')
            ciphertext += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            ciphertext += char
    return ciphertext

def extract_numbers(line):
    numbers = re.findall(r'\d+', line)
    numbers = [int(num) for num in numbers]
    return numbers[1], numbers[2]

def extract_classical_chosen(line):
    classical_chosen = re.findall(r"'(.*?)'", line)
    print(f'classical_chosen = {classical_chosen[0]}')
    return classical_chosen[0]

def extract_vigenere_info(line):
    classical_chosen, classical_key_chosen = re.findall(r"'(.*?)'", line)
    return classical_chosen, classical_key_chosen

def main():
    # test 
    # io = process('python3 flashtime.py', shell=True)
    # netcat
    io = remote('0.0.0.0', 13339)

    while True:
        line = io.recvline().decode()

        if "First one fellas!!" in line:
            num1, num2 = extract_numbers(line)
            answer = str(num1 + num2)
            io.sendline(answer)
        elif "Go on..." in line:
            num1, num2 = extract_numbers(line)
            answer = str(num1 * num2)
            io.sendline(answer)
        elif "Holy.. You're fast..." in line:
            num2, modulo = extract_numbers(line)
            answer = str(num2 % modulo)
            io.sendline(answer)
        elif "Keep up the speed!!" in line:
            modulo, num2 = extract_numbers(line)
            answer = str(pow(num2, -1, modulo))
            io.sendline(answer)
        elif "Almost there!!!" in line:
            num1, num2 = extract_numbers(line)
            answer = str(num1 ** num2)
            io.sendline(answer)
        elif "How are you so good at this?!" in line:
            tetration_chosen, tetration_num = extract_numbers(line)
            answer = str(tetration_answer(tetration_num, tetration_chosen))
            io.sendline(answer)
        elif "Ah yes.. the classics.." in line:
            classical_chosen = extract_classical_chosen(line)
            answer = caesar_cipher(classical_chosen, 3)
            io.sendline(answer)
        elif "LAST QUESTION!!" in line:
            classical_chosen, classical_key_chosen = extract_vigenere_info(line)
            answer = vigenere_cipher(classical_chosen, classical_key_chosen)
            io.sendline(answer)
            print(io.recvall().decode().strip())
            break

if __name__ == "__main__":
    main()