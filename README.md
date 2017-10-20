# Encryption-Decryption-Application
This repository contains a python application that is used for encryption/decryption.

This application uses a columnar transposition in order to perform its encryption. It currently has a basic GUI that asks whether the user wants to encrypt or decrypt. Once the user selects one of the two, it opens a new window requesting the text for encryption/decryption and the key.

Currently, the text that can be encrypted/decrypted is limited to letters; no numbers are allowed. The key can be a mix of numbers and letters.

The decrypted results omits all spaces.

The GUI API can be found in the appJar folder. appJar is the API that I chose to use for this application.

The application itself can be found in the columnar.py file, which contains both the functions for the encryption/decryption as well as the code for running the GUI itself.
