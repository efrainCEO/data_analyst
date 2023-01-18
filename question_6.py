# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 16:48:01 2023

@author: Efrain Santos Luna

@mail: efrain.santos.consultor@gmail.com

@phone:55-66-18-62-95
"""

def search_missing_number(bad_array:list)->int:
    """
    This function looks for the missing number in a list with numbers from 1 to 100
    The way to find the number is based on the sum of all the numbers
    between 1 and 100, later subtracting from this number the sum of the numbers
    from the list with the lost number

    Parameters
    ----------
    bad_array : list
        List from 1 to 100 with a missing number.

    Returns
    -------
    missing_number: int
        missing number in bad_array list.

    """
    total_sum = 5050
    sum_bad_array = sum(bad_array)
    missing_number = total_sum-sum_bad_array
    
    return missing_number

def prove_anagrams(word1:str, word2:str)->bool:
    """
    This function checks if two words are anagrams

    Parameters
    ----------
    word1 : str
        word 1.
    word2 : str
        word 2.

    Returns
    -------
    bool
        true if words are anagrams, otherwise false.

    """
    anagram = False
    word1 = list(word1)
    for letter in word2:
        word1.remove(letter)
    if word1 == []:
        anagram = True
        
    return anagram
    
#lista con numeros del 1 al 100
bad_array = list(range(1,101))
#quito un numero a mi eleccion para simular el numero faltante
bad_array.remove(89)
missing_number = search_missing_number(bad_array)
print('the missing number is: ', missing_number)

'''check if two words are anagrams'''
word_1 = 'dafea'
word_2 = 'fedaa'
is_anagram = prove_anagrams(word_1,word_2)
print('the words are anagram: ', is_anagram)
