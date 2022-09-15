#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:48:48 2021

@author: federico
"""
#libraries 
from subprocess import PIPE, run
import os

#in order to execute shell commands and save their output
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

#the command to decrypt
command0="openssl enc -d -aes-256-cbc -md md5 -in outfile.txt.enc -out file.txt -k "

#read the file and create a list with all the words from the dictionary
with open("google-10000-english-no-swears.txt") as file:
    lines = file.readlines()
    lines = [line.strip() for line in lines]

#replacing all 'o' with '0' as the hint given
for item in lines:
    print(item)
    item=item.replace('o','0')
    password=item.lower()
    
    #run the command appending that password
    command= command0.__add__(password)
    res=os.system(command)
    print(res)
    #if the decrypting process is ok then exit the cycle
    if(res!=256):
        print(password)
        #see if the file is ASCII text and in this case exit the program, otherwise
        #a new cycle is started
        my_output = out("file file.txt")
        print(my_output)
        if("ASCII" in my_output):
            break
         
            

   