# OMC Encryption

# Problem
[openmindsclub](https://openlmindsclub.com) would you like to make an encryption based on no-key system and on binary encoding for there short texts between managers and co-workers.

So you come with great idea which encrypts these messages.

this encryption is described as following:
- giving a string of n letters, **n** <= 1027.
- string **"a"** will be the byte encoding of the **n** number in 8 bytes.
- only lowercase gets encrypted.
- uppercases should get changed to lowercases.
- numbers **1** and **0** are presented as **-1** and **-0**.
- no special characters in the message.
# Task
Make two fonctions `makeItMessy` and `makeItClear`.

Function *makeItMessy* takes **text** a string from the user. this text should get encrypted

Function *makeItClear* takes **binarytext** an encrypted string from the user you should decrypt
# Example
the encryption of  **ABcd03** is  `00000110000001110000100000001001-03`
# Explanation
the following encryption ABcd03. length of ABcd03 is **6**, which means that **"a"** is 00000110.

the encryption will go as following:

 A = **a** = 00000110 | B = **b** = 00000111| **c** = 00001000 | **d** = 00001001|
 
 **0** = -0 | **3** = 3

**ABcd03** == `00000110000001110000100000001001-03`

decrypting `00000110000001110000100000001001-03` == **abcd03**


**Hint:** Use the pre-defined functions [bin( )](https://www.programiz.com/python-programming/methods/built-in/bin) and [int( )](https://www.datacamp.com/community/tutorials/python-data-type-conversion).
