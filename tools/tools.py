"""
*   version 1.0
*   author : david
*   desc : various tools for the project
*    dictionary, letters for string generation...
"""


#Definition of key characteristics constants
CODE_BIN = '1'
CODE_INT= '2'
CODE_HEXA = '3'
CODE_STR = '4'
CODE_READ = '0' #advise don't touch this value, let it to 0
CODE_ASCII = '0'
CODE_4WORD = '2'
CODE_PASSPHRASE = '3'
CODE_CAP = '0'
CODE_SPE_CHAR = '1'

def key_carac_str_to_char(carac):
    """enter the text str corresponding to the CODE_BIN, CODE... and return a char '1', '2'..."""
    if carac == "CODE_BIN":
        return '1'
    elif carac == "CODE_INT":
        return '2'
    elif carac == "CODE_HEXA":
        return '3'
    elif carac == "CODE_STR":
        return '4'
    elif carac == "CODE_READ":
        return '0'
    elif carac == "CODE_ASCII":
        return '0'
    elif carac == "CODE_4WORD":
        return '2'
    elif carac == "CODE_PASSPHRASE":
        return '3'
    elif carac == "CODE_CAP":
        return '0'
    elif carac == "CODE_SPE_CHAR":
        return '1'
    else:
        return None
        

def alphabetic_letters(first, last, tab):
    """return the letters of the alphabet"""
    if tab is None:
        tab = []
    for i in range(first, last):
        tab.append(chr(i))
    return tab
    
      
ALPHABETIC_LETTERS_SMALL = alphabetic_letters(97, 123, None)
ALPHABETIC_LETTERS_CAPITAL = alphabetic_letters(65, 91, None)
NUMERICAL_LETTERS = alphabetic_letters(48, 58, None)
SPECIAL_CHAR_LETTERS = alphabetic_letters(33, 48, None) + alphabetic_letters(58, 65, None) + alphabetic_letters(91, 97, None) + alphabetic_letters(123, 127, None)


def choose_subset_letter(code):
    """choose the alphabetic corresponding to the code
    return all the letters"""
    if(code == CODE_CAP):
        return ALPHABETIC_LETTERS_CAPITAL
    if(code == CODE_INT):
        return NUMERICAL_LETTERS
    if(code == CODE_SPE_CHAR):
        return SPECIAL_CHAR_LETTERS