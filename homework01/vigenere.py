import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for index, x in enumerate(plaintext):
        if x != " ":
            number = upper.find(x)
            if number == -1:
                number = lower.find(x)
                if number == -1:
                    ciphertext += x
                else:
                    key = lower.find(keyword[index % len(keyword)])
                    result = (number + key) % len(lower)
                    ciphertext += lower[result]
            else:
                key = upper.find(keyword[index % len(keyword)])
                result = (number + key) % len(upper)
                ciphertext += upper[result]
        else:
            ciphertext += " "
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for index, x in enumerate(ciphertext):
        if x != " ":
            number = upper.find(x)
            if number == -1:
                number = lower.find(x)
                if number == -1:
                    plaintext += x
                else:
                    key = lower.find(keyword[index % len(keyword)])
                    result = (number - key) % len(lower)
                    plaintext += lower[result]
            else:
                key = upper.find(keyword[index % len(keyword)])
                result = (number - key) % len(upper)
                plaintext += upper[result]
        else:
            plaintext += " "
    return plaintext
