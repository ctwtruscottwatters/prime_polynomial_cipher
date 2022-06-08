# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:46:14 2022
Polynomial cipher using Primes and Bitwise Logic
I love MIT

Authored by Charles Truscott Watters

runfile('C:/Users/Charles_Truscott/Desktop/linearpolycipher.py', wdir='C:/Users/Charles_Truscott/Desktop')
Plain text: 
The quick brown fox jumps over the lazy white rabbit. Charles Truscott. Mark Watters. Tai Truscott. June Truscott. Kerri-Ann Truscott. Byron Bay NSW 2481, Coogee, Bronte, Ballina and Kirra
Cipher text: 
[58656445, 58656465, 58656490, 58656489, 58656438, 58656442, 58656462, 58656488, 58656464, 58656489, 58656491, 58656443, 58656468, 58656444, 58656471, 58656489, 58656495, 58656468, 58656417, 58656489, 58656467, 58656442, 58656466, 58656441, 58656440, 58656489, 58656468, 58656447, 58656490, 58656443, 58656489, 58656445, 58656465, 58656490, 58656489, 58656469, 58656486, 58656419, 58656414, 58656489, 58656444, 58656465, 58656462, 58656445, 58656490, 58656489, 58656443, 58656486, 58656491, 58656491, 58656462, 58656445, 58656489, 58656489, 58656488, 58656465, 58656486, 58656443, 58656469, 58656490, 58656440, 58656489, 58656445, 58656443, 58656442, 58656440, 58656488, 58656468, 58656445, 58656445, 58656489, 58656489, 58656466, 58656486, 58656443, 58656464, 58656489, 58656444, 58656486, 58656445, 58656445, 58656490, 58656443, 58656440, 58656489, 58656489, 58656445, 58656486, 58656462, 58656489, 58656445, 58656443, 58656442, 58656440, 58656488, 58656468, 58656445, 58656445, 58656489, 58656489, 58656467, 58656442, 58656471, 58656490, 58656489, 58656445, 58656443, 58656442, 58656440, 58656488, 58656468, 58656445, 58656445, 58656489, 58656489, 58656464, 58656490, 58656443, 58656443, 58656462, 58656489, 58656486, 58656471, 58656471, 58656489, 58656445, 58656443, 58656442, 58656440, 58656488, 58656468, 58656445, 58656445, 58656489, 58656489, 58656491, 58656414, 58656443, 58656468, 58656471, 58656489, 58656491, 58656486, 58656414, 58656489, 58656471, 58656440, 58656444, 58656489, 58656489, 58656489, 58656489, 58656489, 58656489, 58656489, 58656488, 58656468, 58656468, 58656492, 58656490, 58656490, 58656489, 58656489, 58656491, 58656443, 58656468, 58656471, 58656445, 58656490, 58656489, 58656489, 58656491, 58656486, 58656469, 58656469, 58656462, 58656471, 58656486, 58656489, 58656486, 58656471, 58656493, 58656489, 58656464, 58656462, 58656443, 58656443, 58656486]
Working on decryption but need to lower the order of the polynomial ... 
Letters to decrypt: 

[58656445, 58656465, 58656490, 58656489, 58656438, 58656442, 58656462, 58656488, 58656464, 58656489, 58656491, 58656443, 58656468, 58656444, 58656471, 58656489, 58656495, 58656468, 58656417, 58656489, 58656467, 58656442, 58656466, 58656441, 58656440, 58656489, 58656468, 58656447, 58656490, 58656443, 58656489, 58656445, 58656465, 58656490, 58656489, 58656469, 58656486, 58656419, 58656414, 58656489, 58656444, 58656465, 58656462, 58656445, 58656490, 58656489, 58656443, 58656486, 58656491, 58656491, 58656462, 58656445, 58656489, 58656489, 58656488, 58656465, 58656486, 58656443, 58656469, 58656490, 58656440, 58656489, 58656445, 58656443, 58656442, 58656440, 58656488, 58656468, 58656445, 58656445, 58656489, 58656489, 58656466, 58656486, 58656443, 58656464, 58656489, 58656444, 58656486, 58656445, 58656445, 58656490, 58656443, 58656440, 58656489, 58656489, 58656445, 58656486, 58656462, 58656489, 58656445, 58656443, 58656442, 58656440, 58656488, 58656468, 58656445, 58656445, 58656489, 58656489, 58656467, 58656442, 58656471, 58656490, 58656489, 58656445, 58656443, 58656442, 58656440, 58656488, 58656468, 58656445, 58656445, 58656489, 58656489, 58656464, 58656490, 58656443, 58656443, 58656462, 58656489, 58656486, 58656471, 58656471, 58656489, 58656445, 58656443, 58656442, 58656440, 58656488, 58656468, 58656445, 58656445, 58656489, 58656489, 58656491, 58656414, 58656443, 58656468, 58656471, 58656489, 58656491, 58656486, 58656414, 58656489, 58656471, 58656440, 58656444, 58656489, 58656489, 58656489, 58656489, 58656489, 58656489, 58656489, 58656488, 58656468, 58656468, 58656492, 58656490, 58656490, 58656489, 58656489, 58656491, 58656443, 58656468, 58656471, 58656445, 58656490, 58656489, 58656489, 58656491, 58656486, 58656469, 58656469, 58656462, 58656471, 58656486, 58656489, 58656486, 58656471, 58656493, 58656489, 58656464, 58656462, 58656443, 58656443, 58656486]
Letters decrypted: 

[[58656445], [58656465], [58656490], [58656438], [58656442], [58656462], [58656488], [58656464], [58656491], [58656443], [58656468], [58656444], [58656471], [58656495], [58656468], [58656417], [58656467], [58656442], [58656466], [58656441], [58656440], [58656468], [58656447], [58656490], [58656443], [58656445], [58656465], [58656490], [58656469], [58656486], [58656419], [58656414], [58656444], [58656465], [58656462], [58656445], [58656490], [58656443], [58656486], [58656491], [58656491], [58656462], [58656445], [58656488], [58656465], [58656486], [58656443], [58656469], [58656490], [58656440], [58656445], [58656443], [58656442], [58656440], [58656488], [58656468], [58656445], [58656445], [58656466], [58656486], [58656443], [58656464], [58656444], [58656486], [58656445], [58656445], [58656490], [58656443], [58656440], [58656445], [58656486], [58656462], [58656445], [58656443], [58656442], [58656440], [58656488], [58656468], [58656445], [58656445], [58656467], [58656442], [58656471], [58656490], [58656445], [58656443], [58656442], [58656440], [58656488], [58656468], [58656445], [58656445], [58656464], [58656490], [58656443], [58656443], [58656462], [58656486], [58656471], [58656471], [58656445], [58656443], [58656442], [58656440], [58656488], [58656468], [58656445], [58656445], [58656491], [58656414], [58656443], [58656468], [58656471], [58656491], [58656486], [58656414], [58656471], [58656440], [58656444], [58656488], [58656468], [58656468], [58656492], [58656490], [58656490], [58656491], [58656443], [58656468], [58656471], [58656445], [58656490], [58656491], [58656486], [58656469], [58656469], [58656462], [58656471], [58656486], [58656486], [58656471], [58656493], [58656464], [58656462], [58656443], [58656443], [58656486]]



THEQUICKBROWNFOXJUMPSOVERTHELAZYWHITERABBITCHARLESTRUSCOTTMARKWATTERSTAITRUSCOTTJUNETRUSCOTTKERRIANNTRUSCOTTBYRONBAYNSWCOOGEEBRONTEBALLINAANDKIRRA


"""

import numpy as np
import sys


def find_root(number, root):
    high = number
    low = 0
    guess = (high + low) / 2.0
    epsilon = 0.0000001
    while (guess ** root != number):
        #print("guess: {} high: {} low: {}".format(guess, high, low))
        if guess ** root > number:
            high = guess
        elif guess ** root < number:
            low = guess
        guess = ((high + low) / 2.0)
        if (guess ** root <= number - 0.1):
            break
    return guess
def is_prime(numbers):
    if numbers == 1:
        return True
    for x in range(2, numbers, 1):
        if numbers % x == 0:
            return False
        else:
            return True
def find_primes(start, end):
    if end - start < -8:
        print("Cannot continue ...")
        sys.exit(1)
    nums = []
    primes = []
    for n in range(start, end, 1):
        nums.append(n)
    for n in nums:
        if is_prime(n): primes.append(n)
  
    return primes
def encrypt(string):
    ciphertext = []
    list_of_primes = find_primes(19551993, 19552009)
    #print("The primes used to encrypt the cipher are: {}".format(list_of_primes))
    a = list_of_primes[0]
    b = list_of_primes[1]
    c = list_of_primes[2]
    d = list_of_primes[3]
    e = list_of_primes[4]
    f = list_of_primes[5]
    g = list_of_primes[6]

    
    for n in range(0, len(string), 1):
        numrep = 0
        if string[n] == "A" or string[n] == "a":
            numrep = 1
        elif string[n] == "B" or string[n] == "b":
            numrep = 2
        elif string[n] == "C" or string[n] == "c":
            numrep = 3
        elif string[n] == "D" or string[n] == "d":
            numrep = 4
        elif string[n] == "E" or string[n] == "e":
            numrep = 5
        elif string[n] == "F" or string[n] == "f":
            numrep = 6
        elif string[n] == "G" or string[n] == "g":
            numrep = 7
        elif string[n] == "H" or string[n] == "h":
            numrep = 8
        elif string[n] == "I" or string[n] == "i":
            numrep = 9
        elif string[n] == "J" or string[n] == "j":
            numrep = 10
        elif string[n] == "K" or string[n] == "k":
            numrep = 11
        elif string[n] == "L" or string[n] == "l":
            numrep = 12
        elif string[n] == "M" or string[n] == "m":
            numrep = 13
        elif string[n] == "N" or string[n] == "n":
            numrep = 14
        elif string[n] == "O" or string[n] == "o":
            numrep = 15
        elif string[n] == "P" or string[n] == "p":
            numrep = 16
        elif string[n] == "Q" or string[n] == "q":
            numrep = 17
        elif string[n] == "R" or string[n] == "r":
            numrep = 18
        elif string[n] == "S" or string[n] == "s":
            numrep = 19
        elif string[n] == "T" or string[n] == "t":
            numrep = 20
        elif string[n] == "U" or string[n] == "u":
            numrep = 21
        elif string[n] == "V" or string[n] == "v":
            numrep = 22
        elif string[n] == "W" or string[n] == "w":
            numrep = 23
        elif string[n] == "X" or string[n] == "x":
            numrep = 24
        elif string[n] == "Y" or string[n] == "y":
            numrep = 25
        elif string[n] == "Z" or string[n] == "z":
            numrep = 26
        #print("The character after XOR is : {} ".format(str(int((a ^ numrep) + (b ^ numrep) + (c ^ numrep) + (d ^ e ^ f ^ g)))))
        ciphertext.append(int((a ^ numrep) + (b ^ numrep) + (c ^ numrep) + (d ^ e ^ f ^ g)))


    return ciphertext

def decrypt(encrypted_text, a, b, c, d, e, f, g):
    letters_to_decrypt = encrypted_text
    decrypted_letters = []
    print("Letters to decrypt: \n")
    print(letters_to_decrypt)
    dec_text = ""
    for n in letters_to_decrypt:
        n = [n]
        if n == encrypt("A"):
            dec_text += "A"
            decrypted_letters.append(n)
        if n == encrypt("B"):
            dec_text += "B"
            decrypted_letters.append(n)
        if n == encrypt("C"):
            dec_text += "C"
            decrypted_letters.append(n)
        if n == encrypt("D"):
            dec_text += "D"
            decrypted_letters.append(n)
        if n == encrypt("E"):
            dec_text += "E"
            decrypted_letters.append(n)
        if n == encrypt("F"):
            dec_text += "F"
            decrypted_letters.append(n)
        if n == encrypt("G"):
            dec_text += "G"
            decrypted_letters.append(n)
        if n == encrypt("H"):
            dec_text += "H"
            decrypted_letters.append(n)
        if n == encrypt("I"):
            dec_text += "I"
            decrypted_letters.append(n)
        if n == encrypt("J"):
            dec_text += "J"
            decrypted_letters.append(n)
        if n == encrypt("K"):
            dec_text += "K"
            decrypted_letters.append(n)
        if n == encrypt("L"):
            dec_text += "L"
            decrypted_letters.append(n)
        if n == encrypt("M"):
            dec_text += "M"
            decrypted_letters.append(n)
        if n == encrypt("N"):
            dec_text += "N"
            decrypted_letters.append(n)
        if n == encrypt("O"):
            dec_text += "O"
            decrypted_letters.append(n)
        if n == encrypt("P"):
            dec_text += "P"
            decrypted_letters.append(n)
        if n == encrypt("Q"):
            dec_text += "Q"
            decrypted_letters.append(n)
        if n == encrypt("R"):
            dec_text += "R"
            decrypted_letters.append(n)
        if n == encrypt("S"):
            dec_text += "S"
            decrypted_letters.append(n)
        if n == encrypt("T"):
            dec_text += "T"
            decrypted_letters.append(n)
        if n == encrypt("U"):
            dec_text += "U"
            decrypted_letters.append(n)
        if n == encrypt("V"):
            dec_text += "V"
            decrypted_letters.append(n)
        if n == encrypt("W"):
            dec_text += "W"
            decrypted_letters.append(n)
        if n == encrypt("X"):
            dec_text += "X"
            decrypted_letters.append(n)
        if n == encrypt("Y"):
            dec_text += "Y"
            decrypted_letters.append(n)
        if n == encrypt("Z"):
            dec_text += "Z"
            decrypted_letters.append(n)

#            print(temp_decryption_phrase)
    print("Letters decrypted: \n")
    print(decrypted_letters)
    print("\n\n")
    print(dec_text)
def main():
    print("Plain text: ")
    print("The quick brown fox jumps over the lazy white rabbit. Charles Truscott. Mark Watters. Tai Truscott. June Truscott. Kerri-Ann Truscott. Byron Bay NSW 2481, Coogee, Bronte, Ballina and Kirra. ABCDEFGHIJKLMNOPQRSTUVWXYZ. X Y Z P Q R S AND OR XOR NOT IF AND ONLY IF IF THEN NOT A B C D")
    print("Cipher text: ")
    enc = encrypt("The quick brown fox jumps over the lazy white rabbit. Charles Truscott. Mark Watters. Tai Truscott. June Truscott. Kerri-Ann Truscott. Byron Bay NSW 2481, Coogee, Bronte, Ballina and Kirra. ABCDEFGHIJKLMNOPQRSTUVWXYZ. X Y Z P Q R S AND OR XOR NOT IF AND ONLY IF IF THEN NOT A B C D")
    print(str(enc))
    print("Working on decryption but need to lower the order of the polynomial ... ")
    decrypt(enc, 19551993, 19551995, 19551997, 19551999, 19552001, 19552003, 19552005)
if __name__ == "__main__": main()
