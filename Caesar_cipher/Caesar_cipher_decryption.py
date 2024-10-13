# mono-alphabetic substitution cipher
alphabet_small = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j',
                  'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś',
                  't', 'u', 'w', 'y', 'z', 'ź', 'ż']
alphabet_large = ['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J',
                  'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S', 'Ś',
                  'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż']


# generating the key based on the chosen shift
def generate_the_key():

    shift = 1
    key1 = []
    key2 = []

    for i in range(len(alphabet_small)):
        new_position = (i + shift) % len(alphabet_small)
        key1.append(alphabet_small[new_position])

    for i in range(len(alphabet_large)):
        new_position = (i + shift) % len(alphabet_large)
        key2.append(alphabet_large[new_position])

    return key1, key2


# decrypting the text
def decrypt_the_text(text, key_small, key_large):

    decrypted_text = []

    for letter in text:
        if letter in key_small:
            index = key_small.index(letter)
            decrypted_text.append(alphabet_small[index])
        elif letter in key_large:
            index = key_large.index(letter)
            decrypted_text.append(alphabet_large[index])
        else:
            decrypted_text.append(letter)

    final_decrypted_text = ''.join(decrypted_text)

    return final_decrypted_text


# uploading the file and decrypting it
def upload_the_file():
    key_small_1, key_large_2 = generate_the_key()
    file = 'substitute_proprietary.txt'
    new_file = 'decrypted_caesar.txt'

# utf-8 used to use Polish diacritical marks
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()

    decrypted_text = decrypt_the_text(text, key_small_1, key_large_2)

    with open(new_file, 'w', encoding='utf-8') as f:
        f.write(decrypted_text)

    return text


if __name__ == '__main__':
    upload_the_file()
