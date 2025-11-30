import json
import re
import random
import string

# Caesar cipher encryption and decryption functions (pre-implemented)
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


CAESAR_SHIFT = 3


# Password strength checker function (optional)
def is_strong_password(password):
    """Tarkistaa onko salasana vahva."""
    if len(password) < 8:
        return False

    has_lower = bool(re.search(r"[a-z]", password))
    has_upper = bool(re.search(r"[A-Z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_special = bool(re.search(r"[^A-Za-z0-9]", password))

    return has_lower and has_upper and has_digit and has_special


def generate_password(length):
    """Luo satunnainen vahva salasana (esimerkinomaisesti random-moduulilla)."""
    if length <= 0:
        raise ValueError("Salasanan pituuden on oltava positiivinen.")

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    specials = string.punctuation

    all_chars = lower + upper + digits + specials
    password_chars = []

    if length >= 4:
        password_chars.append(random.choice(lower))
        password_chars.append(random.choice(upper))
        password_chars.append(random.choice(digits))
        password_chars.append(random.choice(specials))
        for _ in range(length - 4):
            password_chars.append(random.choice(all_chars))
        random.shuffle(password_chars)
    else:
        for _ in range(length):
            password_chars.append(random.choice(all_chars))

    return "".join(password_chars)


encrypted_passwords = []
websites = []
usernames = []


# Function to add a new password 
def add_password():
    global encrypted_passwords, websites, usernames

    website = input("Anna sivusto: ").strip()
    username = input("Anna käyttäjätunnus: ").strip()

    use_generator = input("Haluatko generoida vahvan salasanan? (k/e): ").strip().lower()

    if use_generator == "k":
        length_str = input("Anna salasanan pituus (oletus 12): ").strip()
        length = int(length_str) if length_str.isdigit() else 12
        try:
            password = generate_password(length)
            print(f"Luotu salasana: {password}")
        except ValueError as e:
            print(e)
            return
    else:
        password = input("Anna salasana: ")

    # Vahvuustarkistus
    if not is_strong_password(password):
        print("Varoitus: Salasanaa ei pidetä vahvana (min 8 merkkiä, isot, pienet, numero, erikoismerkki).")

    encrypted = caesar_encrypt(password, CAESAR_SHIFT)

    websites.append(website)
    usernames.append(username)
    encrypted_passwords.append(encrypted)

    print("Salasana lisätty onnistuneesti.")


# Function to retrieve a password 
def get_password():
    if not websites:
        print("Ei tallennettuja salasanoja.")
        return

    website = input("Anna sivusto, jolle salasana haetaan: ").strip()

    if website in websites:
        idx = websites.index(website)
        decrypted = caesar_decrypt(encrypted_passwords[idx], CAESAR_SHIFT)
        print(f"\nSivusto:   {website}")
        print(f"Käyttäjä:  {usernames[idx]}")
        print(f"Salasana:  {decrypted}")
    else:
        print("Sivustolle ei löytynyt merkintää.")


# Function to save passwords to a JSON file 
def save_passwords():
    data = []
    for site, user, enc_pw in zip(websites, usernames, encrypted_passwords):
        data.append(
            {
                "website": site,
                "username": user,
                "password": enc_pw,
            }
        )

    try:
        with open("vault.txt", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("Salasanat tallennettu tiedostoon (vault.txt).")
    except OSError as e:
        print(f"Virhe tallennuksessa: {e}")


# Function to load passwords from a JSON file 
def load_passwords():
    global encrypted_passwords, websites, usernames

    try:
        with open("vault.txt", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Tallennustiedostoa ei löytynyt.")
        return
    except json.JSONDecodeError:
        print("Tallennustiedosto on vioittunut tai ei ole JSON-muotoa.")
        return
    except OSError as e:
        print(f"Virhe latauksessa: {e}")
        return

    websites.clear()
    usernames.clear()
    encrypted_passwords.clear()

    for entry in data:
        websites.append(entry.get("website", ""))
        usernames.append(entry.get("username", ""))
        encrypted_passwords.append(entry.get("password", ""))

    print("Salasanat ladattu onnistuneesti.")


# Main method
def main():
    while True:
        print("\nSALASANANHALLINTA")
        print("1. Lisää salasana")
        print("2. Hae salasana")
        print("3. Tallenna salasanat tiedostoon")
        print("4. Lataa salasanat tiedostosta")
        print("5. Lopeta")
        
        choice = input("Valitse toiminto: ")
        
        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            save_passwords()
        elif choice == "4":
            passwords = load_passwords()
        elif choice == "5":
            print("Ohjelma suljetaan.")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")


if __name__ == "__main__":
    main()
