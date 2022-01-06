from string import ascii_letters


def repeat_to_length(s, length):
    return (s * (length // len(s) + 1))[:length]


def encrypt_Vigenere(text: str, key: str):
    result = []
    for i, symbol in enumerate(text):
        # Ci = (Pi + Ki) mod ALPHABET_LEN
        if symbol in ascii_letters:
            encrypted_letter_idx = (ascii_letters.index(symbol)
                                    + ascii_letters.index(key[i])) \
                                   % len(ascii_letters)
            result.append(ascii_letters[encrypted_letter_idx])
        else:
            result.append(symbol)

    return "".join(result)


def decrypt_Vigenere(encrypted_text: str, key: str):
    result = []
    for i, symbol in enumerate(encrypted_text):
        # Pi = (Ci + Ki + ALPHABET_LEN) mod ALPHABET_LEN
        if symbol in ascii_letters:
            decrypted_letter_idx = (ascii_letters.index(symbol)
                                    - ascii_letters.index(key[i])
                                    + len(ascii_letters)) \
                                   % len(ascii_letters)
            result.append(ascii_letters[decrypted_letter_idx])
        else:
            result.append(symbol)
    return "".join(result)


def get_text_from_file(path_to_file: str) -> str:
    try:
        with open(path_to_file, mode='r') as file:
            return file.read()
    except FileNotFoundError:
        print("FILE NOT FOUND")


def write_text_to_file(path_to_file: str, text):
    try:
        with open(path_to_file, mode='w') as file:
            file.write(text)
    except FileNotFoundError:
        print("FILE NOT FOUND")


def encrypt_file():
    print("Input key to encrypt")
    key = input()
    print("Input path to file")

    while True:
        path_to_file = input()
        text = get_text_from_file(path_to_file)
        if text is None:
            continue
        encrypted_text = "".join(
            encrypt_Vigenere(text, repeat_to_length(key, len(text)))
        )
        write_text_to_file('encrypted_file.txt', encrypted_text)
        return True


def decrypt_file():
    print("Input key to encrypt")
    key = input()
    print("Input path to file")

    while True:
        path_to_file = input()
        text = get_text_from_file(path_to_file)
        if text is None:
            continue
        decrypted_file = "".join(
            decrypt_Vigenere(text, repeat_to_length(key, len(text)))
        )
        write_text_to_file('decrypted_file.txt', decrypted_file)
        return True


def main():
    print("Input number to chose action:")
    actions = {
        '1': {'name': 'Encrypt file', 'function': encrypt_file},
        '2': {'name': 'Decrypt file', 'function': decrypt_file}
    }
    for idx, action in actions.items():
        print(f"  {idx} : {action['name']}")

    while True:
        action_choice = input()
        if action_choice in actions:
            break
    result = actions[action_choice]["function"]()
    print(result)


if __name__ == "__main__":
    main()
