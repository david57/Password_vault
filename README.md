# Password_vault
password vault in python multi-user

The password vault is a project for password's storage for some different users.
It can stock a lot of password for different user and using. The password vault contains a key generator.

##########
Take a look in version 1.0 for the beginning of the code
##########

Dependencies :
  - python3
  - tkinter
  - sqlite3
  - ttk

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
 
 
The code generation is made with a decision tree :
Type : (only CODE_STR)                        4
                                              |
Length : (>0)                                 X
                                             /||\
                                           / /  \ \
Text type :                               1 2    3 4
(CODE_BIN, CODE_HEXA,                              |
CODE_INT, CODE_STR)                                |
                                                  / \
Readability : (CODE_READ)                        0   X
                                               /||\  |\
                                              /// |   \\
                                             //|  |    \\
                                            /| |  |     |\
                                           / | |  |     | \
                                          |  | |  |     |  |
String type : 							              0  2 3  4     0  4
                                          |	 | |  |     |  |
Special_char :	(optionnal)				        0	 0 0  0     0  0
(CODE_CAP)								                |  | |  |     |  |
                                          |  | |  |     |  |
                                          |  | |  |     |  | 
Length :								                  X  X X  X     X  X 
                                          |  | |  |     |  | 
(CODE_SPE_CHAR)							              1  1 1  1     1  1
                                          |  | |  |     |  | 
Length :								                  X  X X  X     X  X 
                                          |  | |  |     |  | 
(CODE_CAP)								                2  2 2  2     2  2
                                          |  | |  |     |  | 
Length :								                  X  X X  X     X  X 
