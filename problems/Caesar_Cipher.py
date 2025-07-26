def caesar_cipher(text, shift, decode=False):
    """
    Encrypts or decrypts the given text using Caesar Cipher.
    
    Parameters:
    - text (str): The message to encode or decode.
    - shift (int): The number of positions to shift the letters.
    - decode (bool): If True, it will decode the message.
    
    Returns:
    - str: The encoded or decoded message.
    """
    if decode:
        shift = -shift  # Reverse the shift for decoding

    result = []

    for char in text:
        if char.isalpha():  # Only shift alphabet characters
            base = ord('A') if char.isupper() else ord('a')
            # Shift within the 26-letter alphabet
            offset = (ord(char) - base + shift) % 26
            result.append(chr(base + offset))
        else:
            result.append(char)  # Keep non-alphabet characters as is

    return ''.join(result)

# --- Input from user ---
try:
    operation = input("Do you want to encode or decode the message? (Enter 'encode' or 'decode'): ").strip().lower()
    if operation not in ('encode', 'decode'):
        print("Invalid operation. Please enter 'encode' or 'decode'.")
    else:
        message = input("Enter the message: ")
        shift_value = int(input("Enter the shift value (e.g., 3): "))

        is_decoding = operation == 'decode'
        result = caesar_cipher(message, shift_value, decode=is_decoding)

        print("\nResult:")
        print("Decoded Message:" if is_decoding else "Encoded Message:", result)

except ValueError:
    print("Invalid shift value. Please enter a valid integer.")
