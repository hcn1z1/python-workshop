
import string

def makeItMessy(text : str):
    pass

def makeItClear(encrypted : str):
    pass

if __name__ == "__main__":
    print("""
    1 - Encrypt
    2 - Decrypt""")
    choose = int(input("  Choose :"))
    text = input("  ")
    if choose == 1:print(makeItMessy(text))
    elif choose == 2:print(makeItClear(text))
