#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 01:24:35 2021

@author: federico
"""
input_str = input("Enter the cipher text or plain text: ")
no_of_itr = len(input_str)

for char in "#":
    print(char)
    
    key = char
    output_str = ""
    
    for i in range(no_of_itr):
        current = input_str[i]
        
        output_str += chr(ord(current) ^ ord(key))
    print ("Here's the output: ", output_str)