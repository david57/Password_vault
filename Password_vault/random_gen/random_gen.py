"""
*   version 1.0
*   author : david
*   desc : random generator
*   return a int between 2 values (min, max)
"""
import os
import codecs
from tools.tools import *


class Random_gen:
    """class which generate a random number"""

    ########################
    ##    True type return
    ########################
    @staticmethod
    def generate_int(length):
       """generate a random int number of with length size"""
       return int(str(int(codecs.encode(os.urandom(length), 'hex'), 16))[:length], 10)
   
    @staticmethod
    def generate_int_min_max(min, max):
        """generate a random int between min and max"""
        return (Random_gen.generate_int(max) % (max + 1 - min)) + min

    @staticmethod
    def generate_hex(length):
        """generate a random hex with num size"""
        return codecs.encode(os.urandom(length), 'hex')

    @staticmethod
    def generate_bin(length):
        """define a true binary with num size"""
        return os.urandom(length)


    ##########################
    ##    STR type return
    ##########################
    @staticmethod
    def generate_int_in_str(length):
        """generate a random int in string format for exploitation
        with size of num
        return str type"""
        return str(int(codecs.encode(os.urandom(length), 'hex'), 16))[:length]

    @staticmethod
    def generate_hex_in_str(length):
        """generate a random hex in a string format for exploitation
        with size of num
        return a str value"""
        return str(codecs.encode(os.urandom(length), 'hex'))[2:length + 2]

    @staticmethod
    def generate_bin_in_str(length):
        """generate a random bin in a string format for exploitation
        with size of num
        return a str value"""
        return str("{0:b}".format(int(codecs.encode(os.urandom(length), 'hex'), 16)))[:length]

    #############################
    ##    STRING type generator
    #############################
    @staticmethod
    def random_char(letters):
        """choose a random letters into the letters
        return a char"""
        return letters[Random_gen.generate_int(1000)%len(letters)]
    
    @staticmethod
    def generate_notread_subset(subset, max_length):
        """generate the subset, add to the key
        return the key
        
        IT DOESN'T verify the length of the subset and can exceed the number of subset
        
        IT DOESN'T verify the number of subset in case of collision
        """
        if(type(subset) is not type({'c':'l'})):
           raise TypeError("Bad type for subset")
        dictio = {}
        for i in subset.keys():
            for j in range(1, int(subset[i])+1):
                #subset choice
                letters = choose_subset_letter(i)
                pos = Random_gen.generate_int_min_max(0, max_length)
                l = Random_gen.random_char(choose_subset_letter(i))           
                if pos not in dictio:
                    dictio[pos] = l
        return dictio

    @staticmethod
    def generate_notread_str(letters, length, subset):
        """generate a random string with the alphabetics letters(str or ascii into a tab),
        the length and a subset dictionary to insert into the key
        return a str value"""
        try:
            # we travel the letters' tab and add to the key
            key = ""
            for i in range(1, length+1):
                key += Random_gen.random_char(letters)
            # here we replace the subset into the initial key
            if subset is not None :
                dic = Random_gen.generate_notread_subset(subset, len(key))
                for j in dic.keys():
                    # the assignment doesn't exist in python, so we just create an other str
                    newkey = key[:int(j)] + dic[j] + key[int(j)+1:]
                    key = newkey
            return key
        except TypeError as e:
            print("An error occurred:", e.args[0])
        except:
            print("Error generate_notread_str")
            
    @staticmethod
    def generate_read_str(letters, length, subset):
        """generate a random string with the alhabetics letters(str or ascii into a tab), 
        it is a readable string (alternation consonants vowels)
        return a str value"""
        #not implemented for now
        pass