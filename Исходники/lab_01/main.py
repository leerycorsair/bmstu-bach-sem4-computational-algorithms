import math 
from newtone import newtone_perform
from hermite import hermite_perform

def main():
    mode = int(input("1)Newtone\n2)Hermite\nMode:"))
    if (mode == 1):
        newtone_perform()
    if (mode == 2):
        hermite_perform()

if (__name__ == "__main__"):
    main()
