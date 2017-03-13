from random_gen.random_gen import *
from database.database import *

def test_database():
    db = database('rules.db')
    db.create_tables()
    
    db.insert_rules('bin_court', '4#5#1')
    db.insert_rules('bin_long', '4#36#1')
    db.insert_rules('hexa_court', '4#7#3')
    db.insert_rules('hexa_long', '4#23#3')
    db.insert_rules('int_court', '4#5#2')
    db.insert_rules('int_long', '4#20#2')
