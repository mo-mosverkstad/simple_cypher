import re

def generate_ascii_list(start, stop):
    return [chr(c) for c in range(start, stop)]

def lowcase_list():
    return generate_ascii_list(97, 123)

def upcase_list():
    return generate_ascii_list(65, 91)

def digit_list():
    return generate_ascii_list(48, 58)

def caesar_enc(key):
    k = int(key)
    whole_list = lowcase_list() + upcase_list() + digit_list()
    return dict(zip(whole_list, whole_list[k:]+whole_list[:k]))

def caesar_dec(key):
    k = int(key)
    whole_list = lowcase_list() + upcase_list() + digit_list()
    return dict(zip(whole_list[k:]+whole_list[:k], whole_list))

def handle(plain, profile):
    howto, codec, key = re.split('#', profile)
    func_str = codec + '_' + howto
    codec_dict = eval(func_str)(key)
    #for c in plain:
    #    new_text += codec_dict[c]
    #return new_text
    return ''.join([codec_dict[c] for c in plain])


print(handle('abcdefg', 'enc#caesar#+3')=='defghij')
print(handle('defghij', 'dec#caesar#+3')=='abcdefg')