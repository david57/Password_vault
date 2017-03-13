"""
*   version 1.0
*   author : david
*   desc : design pattern 
*   singleton for using the generate_cor and declare only one time
"""

from cor_generator.cor_generator import *
from rules_gen.rules_gen import *

class Single_cor(object):
    """class singleton for launch the cor and generate the password 
    in function of the code"""
    class __Single_cor:
        def __init__(self):
            #creation of all cor
            self.bin_cor = BIN_COR_Generator()
            self.hex_cor = HEX_COR_Generator()
            self.int_cor = INT_COR_Generator()
            self.ascii_not_read_cor = ASCII_NOT_READ_COR_Generator()
            #set next
            self.bin_cor.set_next(self.hex_cor)
            self.hex_cor.set_next(self.int_cor)
            self.int_cor.set_next(self.ascii_not_read_cor)
        def execute(self, rule):
            """function for execute the resolution by the cor
            return the key generated"""
            if(type(rule) == type(Rules())):
                return self.bin_cor.execute(rule)
            elif(type(rule) == type("")):
                r = Rules()
                return self.bin_cor.execute(r.parse(rule))
    instance = None
    def __new__(cls):
        if not Single_cor.instance:
            Single_cor.instance = Single_cor.__Single_cor()
        return Single_cor.instance
    def __getatt__(self, name):
        return getattr(self.instance, name)
    def __setattr__(self, name):
        return setattr(self.instance, name)
    
#Déclaration de la classe 
SINGLE_COR = Single_cor()