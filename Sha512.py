import hashlib
def generate_hash(text):
    sha512_hash = hashlib.sha512()
    sha512_hash.update(text.encode('utf-8'))
    # Return the hexadecimal representation of the hash
    return sha512_hash.hexdigest()

text = "Hi , this is for Lab 7"
print(text)
hash_code = generate_hash(text)
print(f"SHA-512 hash of text: {hash_code}")
