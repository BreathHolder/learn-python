alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
ten_char_decode_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
unknown_offset_decode_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
vigenere_cipher_message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
code_message = "hello mathew"

def caesar_cipher_decoder(message, offset):
    temp_lst = []
    for char in message:
        if char == ' ' or char == '!' or char == '.' or char == '?' or char == '\'':
            temp_lst.append(char)
        elif alphabet.index(char):
            char_alpha_index = int(alphabet.index(char))
            if char_alpha_index <= len(alphabet) - 1 - offset:                  # was static end of index for for offset of 10, meaning an index <= 15
                cipher_index = char_alpha_index + offset # was an offset == 10
                cipher_char = alphabet[cipher_index]
                temp_lst.append(cipher_char)
            else:
                cipher_index = char_alpha_index - 26 + offset # was an offset of 16 for anything with an index > 15
                cipher_char = alphabet[cipher_index]
                temp_lst.append(cipher_char)
        tester_string = ''.join(temp_lst)
    return tester_string

def caesar_cipher_coder(message, offset):
    temp_lst = []
    for char in message:
        if char == ' ' or char == '!' or char == '.' or char == '?':
            temp_lst.append(char)
        elif alphabet.index(char):
            char_alpha_index = int(alphabet.index(char))
            if char_alpha_index >= 10:
                cipher_index = char_alpha_index - offset
                cipher_char = alphabet[cipher_index]
                temp_lst.append(cipher_char)
            else:
                cipher_index = char_alpha_index + 16
                cipher_char = alphabet[cipher_index]
                temp_lst.append(cipher_char)
        decoded_string = ''.join(temp_lst)
    return decoded_string

# print('1: ', caesar_cipher_decoder(unknown_offset_decode_message, 1))
# print('2: ', caesar_cipher_decoder(unknown_offset_decode_message, 2))
# print('3: ', caesar_cipher_decoder(unknown_offset_decode_message, 3))
# print('4: ', caesar_cipher_decoder(unknown_offset_decode_message, 4))
# print('5: ', caesar_cipher_decoder(unknown_offset_decode_message, 5))
# print('6: ', caesar_cipher_decoder(unknown_offset_decode_message, 6))
print('7: ', caesar_cipher_decoder(unknown_offset_decode_message, 7))
# print('8: ', caesar_cipher_decoder(unknown_offset_decode_message, 8))
# print('9: ', caesar_cipher_decoder(unknown_offset_decode_message, 9))
# print('10: ', caesar_cipher_decoder(unknown_offset_decode_message, 10))
# print('11: ', caesar_cipher_decoder(unknown_offset_decode_message, 11))
# print('12: ', caesar_cipher_decoder(unknown_offset_decode_message, 12))
# print('13: ', caesar_cipher_decoder(unknown_offset_decode_message, 13))
# print('14: ', caesar_cipher_decoder(unknown_offset_decode_message, 14))
# print('15: ', caesar_cipher_decoder(unknown_offset_decode_message, 15))
# print('16: ', caesar_cipher_decoder(unknown_offset_decode_message, 16))
# print('17: ', caesar_cipher_decoder(unknown_offset_decode_message, 17))
# print('18: ', caesar_cipher_decoder(unknown_offset_decode_message, 18))
# print('19: ', caesar_cipher_decoder(unknown_offset_decode_message, 19))
# print('20: ', caesar_cipher_decoder(unknown_offset_decode_message, 20))
# print('21: ', caesar_cipher_decoder(unknown_offset_decode_message, 21))
# print('22: ', caesar_cipher_decoder(unknown_offset_decode_message, 22))
# print('23: ', caesar_cipher_decoder(unknown_offset_decode_message, 23))
# print('24: ', caesar_cipher_decoder(unknown_offset_decode_message, 24))
# print('25: ', caesar_cipher_decoder(unknown_offset_decode_message, 25))
