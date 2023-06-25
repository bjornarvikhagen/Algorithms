from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# CaesarCipher er en enkel substitusjonskryptering som skifter hver bokstav i teksten med en annen en fast avstand unna.
class CaesarCipher:
    @staticmethod
    def encrypt(text, shift):
        result = ""
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) + shift - 97) % 26 + 97)
        return result.encode()

    @staticmethod
    def decrypt(text, shift):
        result = ""
        text = text.decode()
        for i in range(len(text)):
            char = text[i]
            if char.isupper():
                result += chr((ord(char) - shift - 65) % 26 + 65)
            else:
                result += chr((ord(char) - shift - 97) % 26 + 97)
        return result


# AES er en kraftig symmetrisk krypteringsalgoritme som brukes mye i moderne sikkerhetssystemer.
class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        self.iv = get_random_bytes(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.encrypt(pad(data, AES.block_size))

    def decrypt(self, data):
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return unpad(cipher.decrypt(data), AES.block_size)


# RSA er en populær offentlig nøkkel krypteringsalgoritme, noe som betyr at forskjellige nøkler brukes for kryptering og dekryptering.
class RSAEncryption:
    def generate_keypair(self, filename):
        key = RSA.generate(2048)
        private_key = key.export_key()
        public_key = key.publickey().export_key()

        with open(f'{filename}_private.pem', 'wb') as f:
            f.write(private_key)

        with open(f'{filename}_public.pem', 'wb') as f:
            f.write(public_key)

    def encrypt(self, data, filename):
        recipient_key = RSA.import_key(open(f'{filename}_public.pem').read())
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        return cipher_rsa.encrypt(data)

    def decrypt(self, data, filename):
        private_key = RSA.import_key(open(f'{filename}_private.pem').read())
        cipher_rsa = PKCS1_OAEP.new(private_key)
        return cipher_rsa.decrypt(data)


# Test the algorithms
def main():
    # Test Caesar Cipher
    print("Caesar Cipher")
    text = "HELLO"
    shift = 4
    encrypted = CaesarCipher.encrypt(text, shift)
    print(f"Tekst  : {text}")
    print(f"Shift : {shift}")
    print(f"Kryptert: {encrypted}")
    print(f"Dekryptert: {CaesarCipher.decrypt(encrypted, shift)}")
    print()

    # Test AES Cipher
    print("AES Cipher")
    key = get_random_bytes(16)  # AES-nøkkelen må være 16, 24 eller 32 bytes lang
    cipher = AESCipher(key)
    original_data = b'Dette er en test.'  # Dette må være bytes
    encrypted = cipher.encrypt(original_data)
    decrypted = cipher.decrypt(encrypted)
    print(f'Originalt: {original_data}')
    print(f'Kryptert: {encrypted}')
    print(f'Dekryptert: {decrypted}')
    print()

    # Test RSA-kryptering
    print("RSA-kryptering")
    rsa = RSAEncryption()
    filename = "key"
    rsa.generate_keypair(filename)
    original_data = b'Dette er en test for RSA.'
    encrypted = rsa.encrypt(original_data, filename)
    decrypted = rsa.decrypt(encrypted, filename)
    print(f'Originalt: {original_data}')
    print(f'Kryptert: {encrypted}')
    print(f'Dekryptert: {decrypted}')


if __name__ == "__main__":
    main()
