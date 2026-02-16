from shlex import split
import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo.logo)

def encryptMessage (message: str, key: int):
    secureMessage = []
    for letter in message :
        if letter in alphabet:
            position = alphabet.index(letter)
            new_letter = (position + key) % 26
            secureMessage.append(alphabet[new_letter])
            encryptMessage = "".join(secureMessage)
            print(f"Voici le résultat {encryptMessage}")
        else :
            print("Caractère non pris en charge")

def decryptMessage (message: str, key: int):
    secureMessage = []
    for letter in message :
        if letter in alphabet:
            position = alphabet.index(letter)
            new_letter = (position - key) % 26
            secureMessage.append(alphabet[new_letter])
            encryptMessage = "".join(secureMessage)
            print(f"Voici le résultat {encryptMessage}")
        else :
            print("Caractère non pris en charge")

while True :
    role = input("Souhaitez-vous encrypter ou décrypter ? ")
    message = input("Quel est votre message ? ").lower()
    key = int(input("Quelle clé souhaitez-vous ? ( entre 1 et 26 )"))

    if role == "encrypter":
        encryptMessage(message, key)
    else :
        decryptMessage(message, key)

    retry = input("\nSouhaitez-vous recommencer ? ( oui / non)").lower()
    if retry != "oui" :
        break