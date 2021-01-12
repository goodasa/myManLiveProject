import os
import sys

def getfiles():
    fls = []
    for d, sd, fl in os.walk('.'):
        for f in fl:
            fls.append(os.path.join(d, f))
    return list(filter(lambda f: '.pdf' in f, fls))

if __name__ == '__main__':
    print(getfiles()) 
