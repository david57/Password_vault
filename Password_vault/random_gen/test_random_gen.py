from random_gen.random_gen import *
from tools.tools import *

def test_random_gen():
    # generate_int test
    print("test generation int 24 : ")
    for i in range(1, 5):
        print(Random_gen.generate_int(24))

    """print("test generation 1000 random int and verify if the length is ok :")
    for i in range(1, 1000):
        a = Random_gen.generate_int(1024)
        if(len(a) != 1024):
            print("pas bon : " + len(a))"""
            
    #generate_hex test
    print("Test generation hex 24 : ")
    for i in range(1, 5):
        print(Random_gen.generate_hex(24))
        
    """print("test generation 1000 random hex and verify if the length is ok :")
    for i in range(1, 1000):
        a = Random_gen.generate_hex(1024)
        if(len(a) != 1024):
            print("pas bon : " + len(a))"""
            
    print("\nTest generation str 20 :")
    print(Random_gen.generate_notread_str(ALPHABETIC_LETTERS_SMALL, 20, None))
    
    print("Test generation str 20 subset capitale :")
    print(Random_gen.generate_notread_str(ALPHABETIC_LETTERS_SMALL, 20, {'0': '3'}))
    
    print("Test generation str 20 subset nombre :")
    print(Random_gen.generate_notread_str(ALPHABETIC_LETTERS_SMALL, 20, {'2': '3'}))
    
    print("Test generation str 20 subset special char :")
    print(Random_gen.generate_notread_str(ALPHABETIC_LETTERS_SMALL, 20, {'1': '3'}))
    
    print("Test geneation str 20 subset capitale, nombre, spe :")
    print(Random_gen.generate_notread_str(ALPHABETIC_LETTERS_SMALL, 20, {'0':'2', '1':'2', '2':'2'}))
    
    #END
    print("End of the test")