import typing as tp

m='abcdefghijklmnopqrstuvwxyz'
b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
    for index, x in enumerate(plaintext):
        if x != ' ':
            t = b.find(x)
            if t == -1:
              t = m.find(x)
              if t == -1:
                ciphertext += x
              else:
                r = (t + shift) % len(m)
                ciphertext += m[r]
            else:
              r = (t + shift) % len(b)
              ciphertext += b[r]
        else:
            ciphertext += ' '
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
    for index, x in enumerate(ciphertext):
        if x != ' ':
            t = b.find(x)
            if t == -1:
              t = m.find(x)
              if t == -1:
                plaintext += x
              else:
                r = (t - shift) % len(m)
                plaintext += m[r]
            else:
              r = (t - shift) % len(b)
              plaintext += b[r]
        else:
            plaintext += ' '
    return plaintext 
    
print(decrypt_caesar(""))

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
    while (plaintext not in dictionary):
       best_shift += 1
       plaintext = ""
       for index, x in enumerate(ciphertext):
           if x != ' ':
               t = b.find(x)
               if t == -1:
                 t = m.find(x)
                 if t == -1:
                   plaintext += x
                 else:
                   r = (t - best_shift) % len(m)
                   plaintext += m[r]
               else:
                 r = (t - best_shift) % len(b)
                 plaintext += b[r]
           else:
               plaintext += ' '
    return(best_shift)
    
