# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:46:14 2022
Polynomial cipher using Primes
I love MIT

Authored by Charles Truscott Watters
"""

import numpy as np
import sys


def find_root(number, root):
    high = number
    low = 0
    guess = (high + low) / 2.0
    epsilon = 0.0000001
    while (guess ** root != number):
        print("guess: {} high: {} low: {}".format(guess, high, low))
        if guess ** root > number:
            high = guess
        elif guess ** root < number:
            low = guess
        guess = ((high + low) / 2.0)
        if (guess ** root <= number - 0.00001):
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
    ciphertext = ""
    list_of_primes = find_primes(19551993, 19552009)
    print("The primes used to encrypt the cipher are: {}".format(list_of_primes))
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
        ciphertext += str(a * numrep ** 5 + b * numrep ** 4 + c * numrep ** 3 + d + e + f + g ** 2)
        ciphertext += "\n"

    return ciphertext

def decrypt(string, a, b, c, d, e, f, g):
    letters_to_decrypt = []
    decrypted_letters = []
    tempstr = ""
    for x in range(len(string) - 1):
        tempstr += string[x] 
        if string[x + 1] == "\n":
            tempstr += string[x]
            letters_to_decrypt.append(tempstr)
            tempstr = ""
        if string[x] == "\n":
            continue
    for n in letters_to_decrypt:
        print(int(n))
        decrypted_letters.append(int(n) - find_root(g, 2) - f - e - d - int(find_root(int(n), 3)) / c - find_root(int(n), 4) / b - find_root(int(n), 5) / a)
#            print(temp_decryption_phrase)
    print(decrypted_letters)
def main():
    print(encrypt("Charles Thomas Wallace Truscott. Mark William Watters. Tai William Wedekind Truscott"))
    decrypt(encrypt("Charles Thomas Wallace Truscott. Mark William Watters. Tai William Wedekind Truscott"), 19552005, 19552003, 19552001, 19551999, 19551997, 19551995, 19551993)
if __name__ == "__main__": main()
