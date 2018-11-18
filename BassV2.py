# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 08:37:06 2018

@author: rba21
"""
#! python3

import bassmod, random

instances = ""

choice = 0
note = ""


x = 1
strs = "a"

print("\nWelcome to Bass Tool!\n")
print("As to the particular bass guitar... ")

while strs != "4" and strs != "5":
    strs = input("Enter number of strings (4 or 5): ")

b1 = bassmod.Bass(strings = int(strs), frets = 20)
fretboard = b1.create()

def testdown(x, y):
    for fret in range(b1.frets, 0, -1):
        ans = input(x + " string fret " + str(fret) + "? ")
        if ans.upper() == fretboard[y][fret]:
            print("Correct!")
        else:
            print("Sorry. The correct answer is " + fretboard[y][fret] + ".")

def test(x, y):
    for fret in range(1, b1.frets + 1):
        ans = input(x + " string fret " + str(fret) + "? ")
        if ans.upper() == fretboard[y][fret]:
            print("Correct!")
        else:
            print("Sorry. The correct answer is " + fretboard[y][fret] + ".")

def testrand():
    if strs == "4":
        indx = random.randint(0, 3)
        string = "EADG"[indx]
    elif strs == "5":
        indx = random.randint(0, 4)
        string = "BEADG"[indx]
    else:
        print("\nStrings must be 4 or 5")
    f = random.randint(1, 20)
    ans = input(string + " string, fret " + str(f) + "? ")
    if ans.upper() == fretboard[indx][f]:
        print("Correct!")
    else:
        print("Sorry. It's " + fretboard[indx][f])
        
            
def choose():
    ans = ""
    while not ans.isdecimal():
        ans = input("Enter number: ")
    return ans

def testmenu():
    print("\n\n            Test Menu")
    print()
    print("Note: For uniformity, use # for all non-natural notes.")
    print("      (Sharps and flats)")
    print()
    print("1. Test notes ascending")
    print("2. Test notes descending")
    print("3. Test random notes")
    print("4. Cycle of 4ths")
    print("5. Main Menu")
    print("6. Quit program")
    ans = choose()
    if ans == "1":
        x = "H"
        if strs == "5":
            while x not in "abdegABDEG":
                x = input("Which string? (B,E,A,D or G) ").upper()
            strnames = 'BEADG'
            y = strnames.find(x)
            test(x, y)
        elif strs == "4":
            while x not in "adegADEG":
                x = input("Which string? (E,A,D or G) ").upper()
            strnames = 'EADG'
            y = strnames.find(x)
            test(x, y)
        bassmod.pause()
        testmenu()
    elif ans == "2":
        x = "H"
        if strs == "5":
            while x not in "abdegABDEG":
                x = input("Which string? (B,E,A,D or G) ").upper()
            strnames = 'BEADG'
            y = strnames.find(x)
            testdown(x, y)
        elif strs == "4":
            while x not in "adegADEG":
                x = input("Which string? (E,A,D or G) ").upper()
            strnames = 'EADG'
            y = strnames.find(x)
            testdown(x, y)
        bassmod.pause()
        testmenu()
    elif ans == "3":
        z = "H"
        while z not in "nN":
            testrand()
            z = input("Another? (y or n): ")
        testmenu()
    elif ans == "4":
        print('Key of C:  C, F, B flat, E flat, A flat, D flat, G flat, B, E, A, D, G, C')            
    elif ans == "5":
        main()
    else:
        print("Thanks for using Bass Tool")
        bassmod.pause()




def main():
    print("\n     MAIN MENU")
    print()
    print("1. Find all instances of a note")
    print("2. Test knowledge of notes on fretboard")
    print("3. Display all fretboard notes")
    print("4. Exit")
    print()
    choice = int(choose())
    global b1
    if choice == 1:
        b1.instances()
        main()
    elif choice == 2:
        testmenu()
    elif choice == 3:
        fretboard = b1.create()
        b1.show_fretboard()
        print()
        main()
    else:
        print("\nThanks for using Bass Tool.")

main()



