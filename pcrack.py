#!/usr/bin/python
#This program finds collisions for 4 different hashing algorithms.
import hashlib
import os

def md5(string):
    m = hashlib.md5()
    m.update(string)
    return m.hexdigest()

def sha256(string):
    m = hashlib.sha256()
    m.update(string)
    return m.hexdigest()

def sha512(string):
    m = hashlib.sha512()
    m.update(string)
    return m.hexdigest()

def sha1(string):
    m = hashlib.sha1()
    m.update(string)
    return m.hexdigest()

counter = 0

with open("hashes.txt", "r") as myfile:
    hashes = myfile.read()
hashes = hashes.split("\n")[:-1]
while(True):
    for has in hashes:
        #print has
#UNCOMMENT ONLY ONE OF THE FOLLOWING LINES
        ans = md5(str(counter))
        #print ans[:-(len(ans)-len(has))]
        #ans = sha256(str(counter))
        #ans = sha512(str(counter))
        #ans = sha1(str(counter))
        #print ans[:-(len(ans)-len(has))]
        if(ans[:-(len(ans)-len(has))] == has):
            print "DING DING DING DING DING"
            print has + ": " + str(counter)
            string = has + ": " + str(counter)
            os.system("echo " + string + " >> answers.txt")
            hashes.remove(has)
            if(len(hashes) == 0):
                os.system("cat answers.txt")
                exit()
    counter += 1
