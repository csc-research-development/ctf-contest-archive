from timedinput import *
from sympy import *
import random
import re

def extract_number(line):
    number = re.findall(r'\d+', line)
    return int(number[0])

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

def generator():
    num1 = random.randint(1, 10)
    modulo = random.choice([p for p in range(2, 50) if isprime(p)])
    num2 = random.randint(1, modulo - 1)
    
    tetration_choice = ["1st", "2nd", "3rd"]
    tetration_chosen = random.choice(tetration_choice)
    tetration_num = random.randint(3, 5)
    
    classical_choice = ["Wrth", "HRVY", "ZEROBASEONE", "Robin", "Firefly", "Skibidi", "Ohio"]
    classical_chosen = random.choice(classical_choice)
    classical_key = ["Pew", "Lit", "Sus", "Huh", "Wot", "Pie", "Nice"]
    classical_key_chosen = random.choice(classical_key)
    
    questions = [
        f"1. First one fellas!! What is the result of {num1} + {num2}?",
        f"2. Go on... What is the result of {num1} * {num2}?",
        f"3. Holy.. You're fast... Anyways what is the result of {num2} mod {modulo}?",
        f"4. Keep up the speed!! What is the modular inverse of {modulo} mod {num2}?",
        f"5. Almost there!!! What is the result of {num1} raised to the power of {num2}?",
        f"6. How are you so good at this?! Hmph, try this!! What is the {tetration_chosen} tetration of {tetration_num}?",
        f"7. Ah yes.. the classics.. What is the Caesar Cipher encryption of '{classical_chosen}' with a shift of 3?",
        f"8. LAST QUESTION!! What is the Vigenere Cipher encryption of '{classical_chosen}' with a key of '{classical_key_chosen}'?"
    ]
    
    tetration_chosen = extract_number(tetration_chosen)
    answers = [
        str(num1 + num2),
        str(num1 * num2),
        str(num2 % modulo),
        str(pow(num2, -1, modulo)),
        str(num1 ** num2),
        str(tetration_answer(tetration_num, tetration_chosen)),
        caesar_cipher(classical_chosen, 3),
        vigenere_cipher(classical_chosen, classical_key_chosen)
    ]
    return questions, answers

def ask_questions(questions, answers):
    for i in range(len(questions)):
        print(questions[i])
        user_input = timedinput("Your answer : ", timeout=2, default="NOT FAST ENOUGH FLASH").strip()
        
        if user_input == "NOT FAST ENOUGH FLASH":
            print(user_input)
            exit(0)
        
        if user_input != answers[i]:
            print("Incorrect!")
            exit(0)
        else:
            print("That is correct!")
    print()
    print("Congratulations! You've become one with the Speed Force.")
    print()
    print("Here's your reward: CSC{My name is Barry Allen. And I am the fastest man alive. When I was a child I saw my mother killed by something impossible. My father went to prison for her murder. Then an accident made me the impossible. To the outside world I am an ordinary forensic scientist, but secretly I use my speed to fight crime and find others like me. And one day, I'll find who killed my mother and get justice for my father. I am The Flash.}")
    print()
    exit(0)

if __name__ == "__main__":
    questions, answers = generator()
    ask_questions(questions, answers)
