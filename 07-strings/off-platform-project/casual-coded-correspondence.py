from posixpath import split


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def caesar_cipher_decoder(message):
    return 0

storage = []

example_string = "hello mathew"
example_string_list = example_string.rsplit()
print(example_string_list)
example_string_list_letters = str(example_string_list[0])
print(example_string_list_letters)
for char in example_string_list_letters:
    storage.append(char)
print(storage)