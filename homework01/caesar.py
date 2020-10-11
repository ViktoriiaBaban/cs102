import typing as tp
import string


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for x in plaintext:
        if x != " ":
            number = string.ascii_uppercase.find(x)
            if number == -1:
                number = string.ascii_lowercase.find(x)
                if number == -1:
                    ciphertext += x
                else:
                    result = (number + shift) % len(string.ascii_lowercase)
                    ciphertext += string.ascii_lowercase[result]
            else:
                result = (number + shift) % len(string.ascii_uppercase)
                ciphertext += string.ascii_uppercase[result]
        else:
            ciphertext += " "
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for x in ciphertext:
        if x != " ":
            number = string.ascii_uppercase.find(x)
            if number == -1:
                number = string.ascii_lowercase.find(x)
                if number == -1:
                    plaintext += x
                else:
                    result = (number - shift) % len(string.ascii_lowercase)
                    plaintext += string.ascii_lowercase[result]
            else:
                result = (number - shift) % len(string.ascii_uppercase)
                plaintext += string.ascii_uppercase[result]
        else:
            plaintext += " "
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    >>> d = {"python", "java", "ruby"}
    >>> caesar_breaker_brute_force("python", d)
    0
    >>> caesar_breaker_brute_force("sbwkrq", d)
    3
    """
    best_shift = 0
    plaintext = ciphertext
    while plaintext not in dictionary:
        best_shift += 1
        plaintext = ""
        for x in ciphertext:
            if x != " ":
                number = string.ascii_uppercase.find(x)
                if number == -1:
                    numder = string.ascii_lowercase.find(x)
                    if number == -1:
                        plaintext += x
                    else:
                        result = (number - best_shift) % len(string.ascii_lowercase)
                        plaintext += string.ascii_lowercase[result]
                else:
                    result = (number - best_shift) % len(string.ascii_uppercase)
                    plaintext += string.ascii_uppercase[result]
            else:
                plaintext += " "
    return best_shift
