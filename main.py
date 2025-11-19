# Simple Base64 encoder/decoder
# Created for learning purposes
# Author: Ngsnet Hawarya

import base64

def encode_text(text):
    """Encode text into Base64."""
    text_bytes = text.encode("utf-8")
    encoded = base64.b64encode(text_bytes)
    return encoded.decode("utf-8")

def decode_text(encoded_text):
    """Decode Base64 text back to normal."""
    try:
        encoded_bytes = encoded_text.encode("utf-8")
        decoded = base64.b64decode(encoded_bytes)
        return decoded.decode("utf-8")
    except Exception:
        return "Invalid Base64 input."

if __name__ == "__main__":
    print("Base64 Playground")
    print("-----------------")
    print("1) Encode text")
    print("2) Decode text")
    choice = input("Choose an option (1/2): ")

    if choice == "1":
        user_text = input("Enter text to encode: ")
        print("Encoded:", encode_text(user_text))

    elif choice == "2":
        user_text = input("Enter Base64 to decode: ")
        print("Decoded:", decode_text(user_text))

    else:
        print("Unknown option.")
