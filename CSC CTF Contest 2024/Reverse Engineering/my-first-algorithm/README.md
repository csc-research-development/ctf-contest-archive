# My First Algorithm

Analysis:

- A Python file is given which contains an algorithm, the algorithm is divided into 2 functions namely the 'telur_orak_arik_diacak_dan_dibalik' function and the 'eksklusif_atau' function. The 'telur_orak_arik_diacak_dan_dibalik' function has 2 parameters and has a function to scramble a byte string. Inside this function there is a rotation caesar cipher algorithm, where the shift is a random number from a range of 6 to 13, after that the byte string will be scrambled and also reversed. The 'eksklusif_atau' function is a regular function. So the byte string is first scrambled in the 'telur_orak_arik_diacak_dan_dibalik' function then it is XORed by the key and also 1 random string in the 'random_str' variable.

Intended solution:

- The output is decrypted using the same algorithm but the order is reversed, for the shift and also XOR from the random string must be bruteforced.