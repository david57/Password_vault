"""
*   version 1.0
*   author : david
*   desc : rules generator 
*   parse the rules into a code 
"""
from tools.tools import *

class Rules:
    """define caracteristics of a ky or password
    This class is personnalisable"""
    def __init__(self):
        """init the class with none values"""
        ##################################
        ## type text
        ##################################
        # type CODE_STR for text key, others are not implemented for now
        self.type = None
        # length of the total key integer
        self.length = None
        # text type (CODE_BIN || CODE_INT || CODE_HEXA || CODE_STR) 
        self.text_type = None
        # readability (CODE_READ || others)
        self.readability = None
        # string type (CODE_ASCII || CODE_STR || CODE_4WORD || CODE_PASSPHRASE)
        self.string_type = None
        # specials characters in dictionary (CODE_CAP || CODE_INT || CODE_SPE_CHAR)
        # it is must be a dictionary code_spe => number
        self.spe_char = {}
        # code associated, it is none before call the function create_code
        self.code = None
        
    #########################
    ## Parts getter setters
    #########################
    def get_type(self):
        return self.type
    
    def set_type(self, value):
        """Now there is no others type that Text"""
        if(value != CODE_STR):
            raise ValueError("Bad type for key type")
        self.type = value
        
    def get_length(self):
        return self.length
    
    def set_length(self, value):
        if(value <= str(0)):
            raise ValueError("Bad length")
        self.length = int(value)
        
    def get_text_type(self):
        return self.text_type
    
    def set_text_type(self, value):
        """it can be changed if new value are added"""
        if(value != CODE_BIN and value != CODE_INT and value != CODE_HEXA and value != CODE_STR):
            raise ValueError("Bad type for text type")
        self.text_type = value
        
    def get_readability(self):
        return self.readability
    
    def set_readability(self, value):
        """if value != CODE_READ the type is non readable"""
        self.readability = value
        
    def get_string_type(self):
        return self.string_type
    
    def set_string_type(self, value):
        """verify the value in function of readability
        if readability == CODE_READ : type available = ascci, str, 4word, passphrase
        else : type available = ascii, str"""
        if(self.readability == CODE_READ):
            if(value != CODE_ASCII and value != CODE_STR and value != CODE_4WORD and value != CODE_PASSPHRASE):
                raise ValueError("Bad type for string type")
        else:
            if(value != CODE_ASCII and value != CODE_STR):
                raise ValueError("Bad type for string type")
        self.string_type = value
        
    def get_spe_char(self):
        """return a dictionary """
        return self.spe_char
    
    def set_spe_char(self, value):
        """verify that each length, each code is right
        no risk of duplicate because of python's dictionary properties"""
        if(type(value) != type({'t':'t'})):
            raise TypeError("Type must be a dictionary")
        for code in value.keys():
            if(code != CODE_CAP and code != CODE_INT and code != CODE_SPE_CHAR):
                raise ValueError("Bad type for dictionary of special char")
            if(int(value[code]) < 0):
                raise ValueError("Bad length for dictionary of special char")
            #verify if the length of subset exceed the length of the key
            n = 0
            for i in self.spe_char:
                n += int(self.spe_char[i])
            n += int(value[code])
            if(n >= self.length):
                raise ValueError("Bad total length for dictionary subset")
            self.spe_char[code] = value[code]
        
    def parse(self, code):
        """this method parse the code and put on an rules class"""
        tab = code.split("#")
        try:
                # we verify that the length of tab is impair
            if(len(tab) % 2 == 0):
                raise ValueError("Bad code format")
                #the first number is the type string for the key code
            self.set_type(tab[0])
                #the second is the length of the key 
            self.set_length(tab[1])
                #the third value is the string type 
            self.set_text_type(tab[2])
                #the fourth value depend of the string type
                #if tab[2] == (CODE_BIN || CODE_INT || CODE_HEXA ) the Rule class is finished
            if(tab[2] == CODE_BIN or tab[2] == CODE_INT or tab[2] == CODE_HEXA):
                return self
            else:
                    # we take the readability ( CODE_READ )
                self.set_readability(tab[3])
                    #we take the string_type (CODE_ASCII || CODE_STR || CODE_4WORD || CODE_PASSPHRASE)
                self.set_string_type(tab[4])
                    # here we verify the subset (special chars)
                    # need a loop and create a dictionary
                if len(tab) > 5:
                    for i in range(5, len(tab), 2):
                        self.set_spe_char({tab[i]: tab[i+1]})
                # the rule is finished
            return self
        except ValueError as e:
            print("An error occurred:", e.args[0])
            
    def create_code(self):
        """this method create the code associated to this rule
        it is necessary for the creation of the rule into the database by the graphical interface"""
        #test the type, only CODE_STR for now
        if(self.type is not CODE_STR):
            raise ValueError("Bad type for Type, only Text allowed for now")
        self.code = self.type + "#"
        self.code += str(self.length) + "#"
        #text_type, if CODE_BIN, INT, HEXA, stop the function and return the code
        self.code += self.text_type
        if(self.text_type is CODE_BIN or self.text_type is CODE_INT or self.text_type is CODE_HEXA):
            return self.code
        self.code += "#"
        #if it is a string type code
        if(self.readability is CODE_READ):
            self.code += self.readability + "#"
        else:
            self.code += CODE_NOT_READ + "#"
        #the string type
        self.code += self.string_type
        for key in self.spe_char:
            self.code += "#" + key + "#" + self.spe_char[key]
        return self.code