# Password_vault
password vault in python multi-user

The password vault is a project for password's storage for some different users.
It can stock a lot of password for different user and using. The password vault contains a key generator.


############################################################################################

Take a look in version 1.0 for the beginning of the code

############################################################################################

Dependencies :
  - python3
  - tkinter
  - sqlite3
  - ttk

############################################################################################

Functionning of the key generator :
The key generator can generate a lot of key with a different format: 
 - binary : "010011001"
 - integer : "123654"
 - hexadecimal : "1654a12e654f321b"
 - not reading ascii : "sdoifuueoiu"
 - not reading string : "dsoiuééùùùé"
 - reading ascii : "ateticoli" 
 - reading string : ""étalorùtinà"
 - 4word : "dictionary#three#shield#hair"
 - passphrase : "my password is impossible to hack"

It is possible for the string type format to add special char, capital letters and numbers.
The 4 word is a choice of 4 word into a dictionary. 
The 4 word and passphrases are not implemented for the moment.

############################################################################################

The rules are stock into a database and are associated with a name :
 - you can associate a key format with a service
 - you can share this database for add new rules into the database
 
Database schema :
| CODE | LABEL |

CODE : "4#10#4#0#2#0#10"
LABEL : "name of the service"

Code format number and corresponding :
 - CODE_BIN : 1
 - CODE_INT : 2
 - CODE_HEXA : 3
 - CODE_STR : 4
 - CODE_READ  0 
 - CODE_ASCII : 0
 - CODE_4WORD : 2
 - CODE_PASSPHRASE : 3
 - CODE_CAP : 0
 - CODE_SPE_CHAR : 1
 
 
############################################################################################

Take a look into the file TreeCode.PNG for more details about the creation of a code.

############################################################################################

This project use the Design Pattern : Chain of responsibility for the creation of a rules. It take in parameter a code or a rules and use the COR DP for use the right key genererator.

############################################################################################

The key generator uses the function urandom() present in os.
import os;
os.urandom()
This function takes random bytes values into the OS. This must be use at the place of random because random use pseudo-random generator and is not efficiency.
urandom use the pseudo-random generator provide by the os, which use the entries of a lot of device (keyboard, mouse, network trafic, cpu frequency, ram memory...).
