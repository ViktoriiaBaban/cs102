import typing as tp


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
       if (ord(x)<65) or ((ord(x)>90) and (ord(x)<97)) or (ord(x)>122):
          ciphertext += x
       else:
           if (ord(x)+shift<65) or ((ord(x)+shift>90) and (ord(x)+shift<97)) or (ord(x)+shift>122):
               ciphertext += chr(ord(x)+shift-26)
           else:
                ciphertext += chr(ord(x)+shift)
    return ciphertext
    
print(encrypt_caesar(""))

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
       if (ord(x)<65) or ((ord(x)>90) and (ord(x)<97)) or (ord(x)>122):
          plaintext += x
       else:
           if (ord(x)-shift<65) or ((ord(x)-shift>90) and (ord(x)-shift<97)) or (ord(x)-shift>122):
               plaintext += chr(ord(x)-shift+26)
           else:
               plaintext += chr(ord(x)-shift)
    return plaintext
    
print(decrypt_caesar(""))

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
