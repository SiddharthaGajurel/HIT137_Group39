
def encrypt_character(char, shift1, shift2):
    
    if 'a' <= char <= 'z':  # lowercase letters
        if char <= 'm':
            shift = shift1 * shift2
        else:
            shift = -(shift1 + shift2)
        return chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

    elif 'A' <= char <= 'Z':  
        if char <= 'M':
            shift = -shift1
        else:
            shift = shift2 ** 2
        return chr((ord(char) - ord('A') + shift) % 26 + ord('A'))

    else:
        return char  


def decrypt_character(encrypted_char, shift1, shift2, original_char=None):
    
    
    if original_char is None:
        return encrypted_char  

    if 'a' <= original_char <= 'z':
        shift = -(shift1 * shift2) if original_char <= 'm' else (shift1 + shift2)
        return chr((ord(encrypted_char) - ord('a') + shift) % 26 + ord('a'))

    elif 'A' <= original_char <= 'Z':
        shift = shift1 if original_char <= 'M' else -(shift2 ** 2)
        return chr((ord(encrypted_char) - ord('A') + shift) % 26 + ord('A'))

    else:
        return encrypted_char


def encrypt_file(shift1, shift2):
    
    with open("raw_text.txt", "r", encoding="utf-8") as file:
        text = file.read()
    
    encrypted_text = "".join(encrypt_character(char, shift1, shift2) for char in text)
    
    with open("encrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(encrypted_text)


def decrypt_file(shift1, shift2):
   
    
    with open("raw_text.txt", "r", encoding="utf-8") as orig_file, \
         open("encrypted_text.txt", "r", encoding="utf-8") as enc_file:
        original_text = orig_file.read()
        encrypted_text = enc_file.read()
    
    decrypted_text = "".join(
        decrypt_character(enc_char, shift1, shift2, orig_char)
        for enc_char, orig_char in zip(encrypted_text, original_text)
    )
    
    with open("decrypted_text.txt", "w", encoding="utf-8") as file:
        file.write(decrypted_text)


def verify_decryption():
    """Check if decryption matches the original text."""
    
    with open("raw_text.txt", "r", encoding="utf-8") as orig_file, \
         open("decrypted_text.txt", "r", encoding="utf-8") as dec_file:
        original = orig_file.read().replace("\r\n", "\n").strip()
        decrypted = dec_file.read().replace("\r\n", "\n").strip()
    
    if original == decrypted:
        print("✅ Decryption successful!")
    else:
        print("❌ Decryption failed!")


if __name__ == "__main__":
    shift1 = int(input("Enter shift1: "))
    shift2 = int(input("Enter shift2: "))

    encrypt_file(shift1, shift2)
    decrypt_file(shift1, shift2)
    verify_decryption()
