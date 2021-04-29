""" Hello, this is me testing
:)
"""


def xor(plainText: str, key: str) -> set:
    """Simple xor cipher"""
    cipherText = ""
    for i in range(len(plainText)):
        cipherText += chr(ord(plainText[i]) ^ ord(key[i%len(key)]))
    return cipherText


if __name__ == "__main__":
    # Testing
    plainText = input("Plain text: ")
    key = input("Key: ")

    print(f"Cipher text: {xor(plainText, key)}")
