m = 'abcdefghijklmnopqrstuvwxyz'
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

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
    space = 0
    for index, x in enumerate(plaintext):
        if x != ' ':
            t = b.find(x)
            if t == -1:
              t = m.find(x)
              if t == -1:
                ciphertext += x
              else:
                k = m.find(keyword[index % len(keyword)])
                r = (t + k) % len(m)
                ciphertext += m[r]
            else:
              k = b.find(keyword[index % len(keyword)])
              r = (t + k) % len(b)
              ciphertext += b[r]
        else:
            space +=1
            ciphertext += ' ' 
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
    space = 0
    for index, x in enumerate(ciphertext):
        if x != ' ':
            t = b.find(x)
            if t == -1:
              t = m.find(x)
              if t == -1:
                plaintext += x
              else:
                k = m.find(keyword[index % len(keyword)])
                r = (t - k) % len(m)
                plaintext += m[r]
            else:
              k = b.find(keyword[index % len(keyword)])
              r = (t - k) % len(b)
              plaintext += b[r]
        else:
            space +=1
            plaintext += ' ' 
    return plaintext
