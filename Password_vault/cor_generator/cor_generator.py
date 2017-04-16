"""
*   version 1.0
*   author : david
*   desc : design pattern 
*   chain of responsbility for choose the right key generator
"""
from random_gen.random_gen import *
from rules_gen.rules_gen import *

class COR_Generator:
    """The mother class for the choice of the right generator"""
    def __init__(self):
        self.next = None
        
    def execute(self, rule):
        """we use the polymorphism for launch the daughter function"""
        pass
    
    def set_next(self, next):
        if(COR_Generator is not None):
            self.next = next
            
    def get_next(self):
        return self.next
    
    
class BIN_COR_Generator(COR_Generator):
    """The cor corresponding for the bin key generation"""
    def execute(self, rule):
        """this function verify if the rule correspond to the generation of a binary key
        Next, it generate and return the corresponding key
        if the rule is not the right, the function put to the next cor"""
        try:
            if(rule.type is not CODE_STR or rule.text_type is not CODE_BIN):
                if(self.next is not None):
                    return self.next.execute(rule)
            else:
                return Random_gen.generate_bin_in_str(rule.length)
        except:
            print("Error BIN_COR_Generator")
            
            
class HEX_COR_Generator(COR_Generator):
    """The cor corresponding the hex generation"""
    def execute(self, rule):
        """This function verify if the rule correspond to the generation of a hex Key
        Next, it generate and return the corresponding Key
        if the rule is not the right, the function put to the next cor"""
        try:
            if(rule.type is not CODE_STR or rule.text_type is not CODE_HEXA):
                if(self.next is not None):
                    return self.next.execute(rule)
            else:
                return Random_gen.generate_hex_in_str(rule.length)
        except:
            print("Error HEX_COR_Generator")
            
            
class INT_COR_Generator(COR_Generator):
    """The cor corresponding the int generation"""
    def execute(self, rule):
        """This function verify if the rule correspond to the generation of a int Key
        Next, it generate and return the corresponding Key
        if the rule is not the right, the function put to the next cor"""
        try:
            if(rule.type is not CODE_STR or rule.text_type is not CODE_INT):
                if(self.next is not None):
                    return self.next.execute(rule)
            else:
                return Random_gen.generate_int_in_str(rule.length)
        except:
            print("Error INT_COR_Generator")
            
class ASCII_NOT_READ_COR_Generator(COR_Generator):
    """The cor corresponding to the ascii not readable generation"""
    def execute(self, rule):
        """This function verify if the rule correspond to the generation of a int Key
        Next, it generate and return the corresponding Key
        if the rule is not the right, the function put to the next cor""" 
        try:
            if(rule.type is not CODE_STR or rule.text_type is not CODE_STR):
                if(self.next is not None):
                    return self.next.execute(rule)
            else:
                return Random_gen.generate_notread_str(ALPHABETIC_LETTERS_SMALL, rule.get_length(), rule.get_spe_char())
        except:
            print("Error ASCII_NOT_READ_COR_Generator")     