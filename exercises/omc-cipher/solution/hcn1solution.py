
##    OMC Python Workshop
##    Script By: Mohamed Amine Hammane

import string

def makeItMessy(text : str):
    lowercase = string.ascii_lowercase
    # convert Text to lowercase
    text = text.lower()
    encrypted = ""
    length = len(text)
    '''
        Encrypting the script
        scraping text letter by letter and encrypting
    '''
    for letter in text:
        if letter in lowercase:    # find position of letter in lowercase
            for i in range(len(lowercase)):
                if lowercase[i] == letter:
                    break
            # i  is position of letter in lowercase
            # the encryption is as following
            encrypted += bin(length+i).replace("0b","0"*(8-(len(bin(length+i))-2)))
        elif letter == " ":
            encrypted += " "
        elif letter >= "0" and letter <= "9":
            if letter == "0" or letter == "1": encrypted += "-" + letter
            else: encrypted += letter
    return encrypted


def makeItClear(encrypted : str):
    # looking for length we omit -0 and -1 and numbers
    lowercase = string.ascii_lowercase
    length = len(encrypted)
    real_length = 0
    for letter in encrypted:
        if (letter > "1" and letter <= "9") or (letter == " "): length -= 1; real_length += 1
        elif (letter == "-"): length -= 2; real_length += 1
    real_length += length/8 # 8 bits
    text = ""
    i = 0
    while i < len(encrypted):
        # checking first letter
        if encrypted[i] == "1" or encrypted[i] == "0":
        # now scraping encrypted by 8 bits
        # we shall add "0b" to _8bits to be able to convert it to int
        # example int("0b00101",2) = 5

            _8bits = encrypted[i:i+8]
            _8bits = "0b" + _8bits
            encodingInt = int(_8bits,2)


        # after getting the encoded integer. we gotta convert it to string.
        # and that maybe done by user lowercase and substrcting the real length
        
            huh = encodingInt - real_length
            text += lowercase[int(encodingInt - real_length)]
            i += 8
        elif encrypted[i] == " " or (encrypted[i] > "1" and encrypted[i] <= "9"):
            text += encrypted[i]
            i += 1
        elif encrypted[i] =="-":
            text += encrypted[i+1]
            i += 2
    return text


if __name__ == "__main__":
    print("""
    1 - Encrypt
    2 - Decrypt""")
    choose = int(input("  Choose :"))
    text = input("  ")

    if choose == 1:print(makeItMessy(text))
    elif choose == 2:print(makeItClear(text))
