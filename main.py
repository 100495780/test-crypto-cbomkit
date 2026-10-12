import hashlib
from cryptography.fernet import Fernet

def insecure_hash(data):
    # MD5 es vulnerable (reducido por Grover / colisiones)
    return hashlib.md5(data.encode()).hexdigest()

def encrypt_data():
    # Fernet usa AES en modo CBC con firma HMAC
    key = Fernet.generate_key()
    f = Fernet(key)
    return f.encrypt(b"Datos super secretos")