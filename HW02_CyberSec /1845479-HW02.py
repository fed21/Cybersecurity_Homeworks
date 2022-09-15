#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 14:48:48 2021

@author: federico
"""
#libraries 
from subprocess import PIPE, run
import os
import random

#in order to execute shell commands and save their output
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

#the command to decrypt and the length as input
i=False
command0="openssl enc -des -d -pbkdf2 -in outfile.txt.enc -out file.txt -k "
stop=0
length=input("Insert the length of the password with whom you want to try brute-force: ")
length=int(length)

#until an ASCII text is found
while(i==False):
    stop=0
    #creating random passwords of the length chosen
    while (stop==0):
        ListOfChars=[]
        codes=list(range(48,57))+list(range(65,90))+list(range(97,122))
        for a in range(length):
            ASCIIcode=random.choice(codes)
            ListOfChars.append(chr(ASCIIcode))
        password=''.join(ListOfChars)
        #run the command appending that password
        command= command0.__add__(password)
        res=os.system(command)
        print(res)
        #if the decrypting process is ok then exit the cycle
        if(res!=256):
            print(password)
            stop=1

    #see if the file is ASCII text and in this case exit the program, otherwise
    #a new cycle is started
    my_output = out("file file.txt")
    print(my_output)
    if("ASCII" in my_output):
        i=True
    else: 
        i=False
    print(i)
    

    
   