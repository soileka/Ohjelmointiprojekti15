import unittest
import json
import os
from unittest.mock import patch, mock_open
from main import (
    is_strong_password,
    generate_password,
    add_password,
    get_password,
    save_passwords,
    load_passwords,
    websites,
    usernames,
    encrypted_passwords,
    caesar_decrypt,
    CAESAR_SHIFT
)

class TestPasswordManager(unittest.TestCase):

    def setUp(self):
        # Nollataan globaalit listat ennen jokaista testiä
        websites.clear()
        usernames.clear()
        encrypted_passwords.clear()

        # Luodaan väliaikainen salasanafile testejä varten
        self.test_file = "test_vault.txt"
        self.test_data = [
            {"website": "example.com", "username": "user123", "password": "ABC"},
            {"website": "test.com", "username": "testuser", "password": "XYZ"}
        ]
        with open(self.test_file, "w", encoding="utf-8") as f:
            json.dump(self.test_data, f)

    def tearDown(self):
        # Siivotaan testitiedosto
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    # ---------------------------------------
    # PASSWORD STRENGTH
    # ---------------------------------------
    def test_is_strong_password(self):
        self.assertTrue(is_strong_password("Str0ngP@ssw0rd"))
        self.assertFalse(is_strong_password("Weak123"))
        self.assertFalse(is_strong_password("weakpassword123!"))
        self.assertFalse(is_strong_password("Weakpassword123"))

    # ---------------------------------------
    # PASSWORD GENERATOR
    # ---------------------------------------
    def test_generate_password(self):
        pw1 = generate_password(12)
        self.assertEqual(len(pw1), 12)
        self.assertTrue(is_strong_password(pw1))

        pw2 = generate_password(16)
        self.assertEqual(len(pw2), 16)
        self.assertTrue(is_strong_password(pw2))

    # ---------------------------------------
    # ADD PASSWORD (mock input)
    # ---------------------------------------
    @patch("builtins.input", side_effect=[
        "example.net",     # website
        "user456",         # username
        "e",               # do NOT generate password
        "StrongP@ssw0rd"   # password
    ])
    def test_add_password(self, mock_inputs):
        add_password()

        # Varmentaa että globaalit listat sisältävät merkinnän
        self.assertIn("example.net", websites)
        idx = websites.index("example.net")

        self.assertEqual(usernames[idx], "user456")
        decrypted = caesar_decrypt(encrypted_passwords[idx], CAESAR_SHIFT)
        self.assertEqual(decrypted, "StrongP@ssw0rd")

    # ---------------------------------------
    # GET PASSWORD (mock input + print)
    # ---------------------------------------
    @patch("builtins.print")
    def test_get_password(self, mock_print):
        # Lisätään testidata ohjelman sisäisiin listoihin
        websites.append("example.com")
        usernames.append("user123")
        encrypted_passwords.append("DEF")  # Caesar-salattu "ABC", esimerkki

        with patch("builtins.input", return_value="example.com"):
            get_password()

        # Tulostuksen ensimmäinen argumentti sisältää salasanan viimeisen printin
        output = ""
        for call in mock_print.call_args_list:
            if "Salasana:" in str(call):
                output = str(call)
                break

        self.assertIn("Salasana:", output)

    # ---------------------------------------
    # SAVE PASSWORDS
    # ---------------------------------------
    def test_save_passwords(self):
        # Ladataan testidataa globaaleihin listoihin
        websites.extend(["example.com", "test.com"])
        usernames.extend(["user123", "testuser"])
        encrypted_passwords.extend(["AAA", "BBB"])

        # Tallennetaan testitiedostoon
        save_passwords()

        with open("vault.txt", "r", encoding="utf-8") as f:
            saved = json.load(f)

        self.assertEqual(len(saved), 2)

    # ---------------------------------------
    # LOAD PASSWORDS
    # ---------------------------------------
    def test_load_passwords(self):
        load_passwords()

        self.assertEqual(len(websites), 2)
        self.assertEqual(websites[0], "example.com")

        # Nonexistent file
        if os.path.exists("nonexistent.txt"):
            os.remove("nonexistent.txt")

        load_passwords()  # pitäisi tulostaa virhe, ei kaatua

        # listat eivät muutu
        self.assertEqual(len(websites), 2)


if __name__ == '__main__':
    unittest.main()
