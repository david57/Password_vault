from cor_generator.cor_generator import *
from cor_generator.single_cor import *
from rules_gen.rules_gen import *

def Test_cor_generator():    
    #test binary
    rule = Rules()
    rule.parse("4#10#1")
    key = SINGLE_COR.execute(rule)
    print("Binary key = " + str(key) + "\n")
    
    #test hexa
    rule.parse("4#13#3")
    key = SINGLE_COR.execute(rule)
    print("Hexa key = " + str(key) + "\n")
    
    #test int
    rule.parse("4#9#2")
    key = SINGLE_COR.execute(rule)
    print("Int key = " + str(key) + "\n")