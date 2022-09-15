#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:02:37 2021

@author: federico
"""

import sys 

#initial prints
print("\nWelcome to the frequencies analyzer!")
print("NOTE: It assumes that the plaintext is in English and all in capital letters..")
ciphertext_filename = input("Enter the name of the file with the ciphertext: ")
 
#open text file in read mode
ciphertext_file = open(ciphertext_filename, "r")
 
#read whole file to a string
ciphertext = ciphertext_file.read()
 
#close file
ciphertext_file.close()

#print the ciphertext
print("\nThis is the ciphertext uploaded:")
print(ciphertext)

#analyzing frequencies
num_chars=0
freq_dictionary = {}
for char in ciphertext:
    if char not in freq_dictionary:
        freq_dictionary[char] = 1
    else:
        freq_dictionary[char] += 1
    num_chars+=1

print("\nNow these are the occurences of all the characters in the ciphertext:")
print(freq_dictionary)
print("The number of chars is: ",num_chars)
print("The frequencies of the characters are shown below:")

for key in freq_dictionary:
    freq_dictionary[key] *= 100
    freq_dictionary[key] /= num_chars

sorted_freq_dictionary = {}
sorted_values = sorted(freq_dictionary.values())
for i in sorted_values:
    for k in freq_dictionary.keys():
        if freq_dictionary[k] == i:
            sorted_freq_dictionary[k] = freq_dictionary[k]
            
print("Dictionary sorted by frequence value",sorted_freq_dictionary)

#ask for replaces ("EXIT" to exit the program or "NEW" to return to the original ciphertext)
original_one = ciphertext
while(True):
    char_to_replace = input("\nSelect a char to replace (or 'EXIT' to exit the program or 'NEW' to restart from the original ciphertext): ")
    if(char_to_replace == "EXIT"):
        sys.exit()
    if(char_to_replace == "NEW"):
        ciphertext = original_one
        print("\nRestart from the original one..",ciphertext)
        continue
    char_to_replace_with = input ("\nSelect a char to replace it with: ")
    print("\n")
    ciphertext = ciphertext.replace(char_to_replace,char_to_replace_with.lower())

    print("\nNow the text becomes: ",ciphertext)




