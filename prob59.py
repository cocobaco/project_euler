# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 12:59:36 2021

@author: PC1
"""

# learned and adapted from
# https://radiusofcircle.blogspot.com/2016/06/problem-59-project-euler-solution-with-python.html

# project euler: https://projecteuler.net
# problem 59: XOR decryption


'''
# text + key ==> cyphertext
cypertext + key ==> text

given: encryption key is three lower letters
text is in English

python functions:
    chr turns ascii to character
    ord turns character to ascii
'''
    
from time import time
from string import ascii_lowercase


def xor_op(a, b):
    '''bitwise XOR operator
    0 0 -> 0
    0 1 -> 1
    1 0 -> 1
    1 1 -> 0
    '''
    xor = a ^ b
    return xor


def decrypt(s, t):
    ''' cipher-text (t) XOR encryption key (s) --> original text'''
    orig_chrs = [chr(a ^ ord(b)) for a, b in zip(s, t)]
    orig_text = ''.join(orig_chrs)
    return orig_text
    # return ''.join(chr(a ^ ord(b)) for a, b in zip(s, t))


def check_english(ascii1, ascii2):
    xor = xor_op(ascii1, ascii2)
    # https://simple.wikipedia.org/wiki/ASCII
    # eng_letters_range = list(range(32, 91)) + list(range(97, 123))
    # eng_letters_range = list(range(32, 123))
    eng_letters_range = list(range(32, 94)) + list(range(97, 123))
    if xor in eng_letters_range:
        return True
    return False


def find_valid_keys(idx, idx_step, cipher, poss_key_ascii):
    idxs = range(idx, len(cipher), idx_step)
    ciphers_idx = [cipher[i] for i in idxs]
    
    letter_ascii = set([])
    for k in poss_key_ascii:
        for c in ciphers_idx:
            letter_ascii.add(k)
            if not check_english(c, k):
                letter_ascii.remove(k)
                break
    letter_chr = [chr(l) for l in letter_ascii]
    return letter_chr, letter_ascii
    

def solution():
    file = 'data/p059_cipher.txt'
    
    with open(file, 'r') as f:
        text = f.read()
        
    cipher = list(map(int, text.split(',')))
    
    # key is 3-letter a-z (lower case)
    letters = list(ascii_lowercase)
    # key_ascii_letters = range(97, 123)
    poss_key_ascii = [ord(l) for l in letters]
    ascii_dict = {k:v for k,v in zip(poss_key_ascii, letters)}

    print(ascii_dict)
    
    first_letter_chr, first_letter_ascii = find_valid_keys(0, 3, cipher, 
                                                           poss_key_ascii)
    
    second_letter_chr, second_letter_ascii = find_valid_keys(1, 3, cipher, 
                                                             poss_key_ascii)
    
    third_letter_chr, third_letter_ascii = find_valid_keys(2, 3, cipher, 
                                                           poss_key_ascii)
    
    print(first_letter_chr)
    print(second_letter_chr)
    print(third_letter_chr)
    
    encrypt_keys = []       
    for i in first_letter_chr:
        for j in second_letter_chr:
            for k in third_letter_chr:
                key = i + j + k
                encrypt_keys.append(key)
                
    print(encrypt_keys)
    
    
    # # conver the first letter from ascii to character
    # first_letter = chr(list(first_letter)[0])
    # # first_letter = ascii_dict[first_letter]
    
    # # convert the second letter from ascii to character
    # second_letter = chr(list(second_letter)[0])
    
    # # convert the third letter from ascii to character
    # third_letter = chr(list(third_letter)[0])
    
    # # string concatenation to find the encrypt key
    # encrypt_key = first_letter+second_letter+third_letter
    
    for encrypt_key in encrypt_keys:
        # variable to store the decrypted string
        plain_text = ''
        
        # looping through the cipher text
        for i in range(0, len(cipher), 3):
            plain_text += decrypt(cipher[i:i+3], encrypt_key)
        
        print(f'using key {encrypt_key}, the original text is:\n{plain_text}')
        
        # printing the sum of characters
        ans = sum(map(ord, plain_text))
        print(ans)

    return ans


def report():
    print(('sum of the ASCII values in the original text '
           f'is {solution()}'))


def main():
    tic = time()
    
    # projecteuler number:
    report()
    # 
    
    toc = time()
    
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()