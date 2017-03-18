#!/usr/bin/env python3
# coding=UTF-8
import sys
import hashlib

def nameTransfer(true,nick):
    newStr = str(gcd(nameToNum(true),nameToNum(nick)))
    newNum = [int(i) for i in newStr]
    i = 0
    newName = []
    while i < len(newStr) - 1:
        sNum = abs(int((int(newNum[i] + newNum[i+1])) + (int(newNum[i]) * int(newNum[i+1])) + len(sys.argv[1])*len(sys.argv[2])))
        if sNum > 127 or sNum < 32:
            sNum = abs(int(sNum/10) + 61)
        newName.append(sNum)
        i=i+2
    return "".join(map(chr, newName))

def nameToNum(name):
    t = hashlib.md5(name.encode("UTF-8")).hexdigest()
    return int(t,16)
def gcd(a,b):
    a = int(abs(a-b)%abs(a+b))
    b = int(abs(a+b)%abs(a-b))
    if a < b:
        a, b = b, a
    y = a % b
    if y == 0:
        return b
    else: 
        a, b = b, y
        return gcd(a,b)
if __name__ == "__main__":
    password = str(nameTransfer(sys.argv[1],sys.argv[2]))
    errors = [',','\\','/',':',';','<','>',' ','^',']','[','=','"','!','{','}',"'",'~','(',')']
    for error in errors:
        if password.find(error) > -1:
            password = password.replace(error,'')
    print("\nYour Fucking Strong Password is:\n\n" + '\033[31m' + password)
    print('\033[30m')