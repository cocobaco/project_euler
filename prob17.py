# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 13:30:29 2020

@author: rop
"""

# project euler: https://projecteuler.net
# problem 17: Number letter counts

from time import time

def num_to_text(num):
    map_ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 
                        6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    map_teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 
                 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 
                18: 'eighteen', 19: 'nineteen'}
    map_tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 
                6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
        
    if num < 10:
        num_text = map_ones[num]
    elif 10 <= num < 20:
        num_text = map_teens[num]
    elif num < 100:
        tens_text = map_tens[int(str(num)[0])]
        n_ones = int(str(num)[-1])
        if n_ones == 0:
            ones_text = ''
        else:
            ones_text = map_ones[n_ones]
        num_text = tens_text + ones_text
    elif num < 1000:
        n_hundred = int(str(num)[0])
        hundreds_text = map_ones[n_hundred]
        n_tens_and_ones = int(str(num)[-2:])
        if n_tens_and_ones == 0:
            num_text = hundreds_text + 'hundred'
        elif 10 <= n_tens_and_ones < 20:
            num_text = hundreds_text + 'hundred and' + map_teens[n_tens_and_ones]
        else:
            n_tens = int(str(num)[1])
            if n_tens == 0:
                tens_text = ''
            else:
                tens_text = map_tens[n_tens]
            n_ones = int(str(num)[-1])
            if n_ones == 0:
                ones_text = ''
            else:
                ones_text = map_ones[n_ones] 
            if n_tens == 0:
                num_text = hundreds_text + 'hundred and' + ones_text  
            elif n_ones == 0:
                num_text = hundreds_text + 'hundred and' + tens_text
            elif n_tens == 1 and n_ones == 0:
                num_text = hundreds_text + 'hundred and' + 'ten'
            else:
                num_text = hundreds_text + 'hundred and' + tens_text + ones_text
    elif num == 1000:
        num_text = 'one thousand'
            
    return num_text


def solution(n):
    ans = 0
    for i in range(1, n+1):
        num_text = num_to_text(i)
        num_text = num_text.replace(' ', '').replace('-', '')
        print(i, num_text)
        ans += len(num_text)
        
    return ans


def report(n):
    print(f'if numbers 1 to {n} are written out in words, {solution(n)} letters will be used.')    

    
def main():
    tic = time()
    
    report(5)
    # 19
    
    # projecteuler number:
    report(1000)
    
    
    toc = time()
    print('time used:', toc - tic)
    
    
if __name__ == '__main__':
    main()