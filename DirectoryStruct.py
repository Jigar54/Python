import os
import time
import sys


def getdir(x, level):
    if (not(os.access(x, os.X_OK or OS.R_OK))):
        print (level-1)*" "*5,
        print "#----------Folder Name:",
        print os.path.basename(x)+"/",
        print "----------#"
        print level*" "*8,
        print "No Permissions access this directory!\n"
        return
    y = os.listdir(x)
    z = os.listdir(x)
    y.sort()
    z.sort()
    global ctr
    global dirctr
    print (level-1)*" "*5,
    print "#----------Folder Name:",
    print os.path.basename(x)+"/",
    print "----------#",
    print (25-level)*" "*2,
    print "Folder Size:",
    print os.path.getsize(x)
    print level*" "*5,
    if (y):
        print "|"
    new = []
    for i in range(len(y)):
        y[i] = x + "/" + y[i]
        if (os.path.isdir(y[i]) == True):
            dirctr += 1
            getdir(y[i], level+1)
        else:
            print (level)*" "*5,
            print "|",
            print "#-"+z[i]+"\t\t\t File Size:",
            ctr += 1
            print os.path.getsize(y[i]),
            print "\tLast Modified ",
            print time.ctime(os.path.getmtime(y[i]))
    if len(y) == 0:
        print level*" "*5,
        print "(Empty Folder)\n"


x = sys.argv[1]
x = os.path.abspath(x)
if (os.path.isdir(x) == False):
    print "DIRECTORY DOESNT EXIST!!"
else:
    l = 1
    dirctr = 0
    ctr = 0
    getdir(x, l)
    print "\n"
    print dirctr,
    print " directories, ",
    print ctr,
    print " files"
