from Crypto.Cipher import AES

KEY = b'mysecretaeskey12'  # 16 bytes = 128-bit key

def pad(data):
    return data + b' ' * (16 - len(data) % 16)

def unpad(data):
    return data.rstrip(b' ')

def encrypt_file(file_data):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return cipher.encrypt(pad(file_data))

def decrypt_file(file_data):
    cipher = AES.new(KEY, AES.MODE_ECB)
    return unpad(cipher.decrypt(file_data))
