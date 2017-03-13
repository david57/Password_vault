"""
*   version 1.0
*   author : david
*   desc : graphical interface or key and rules generation
"""

import tkinter as tk
import tkinter.ttk as ttk
from database.database import *
from cor_generator.single_cor import *
from tools.tools import *
from rules_gen.rules_gen import *
from multiprocessing.managers import State

MAX_LENGTH = 100000


class Graphical:   
    """class for choose if the program load an existing rules or create 
    an other one"""
    def __init__(self):
        """constructor of the graphical interface
        load the database for the rule"""
        self.db = database('rules.db')
        
    def load_rule(self):
        """open the graphical interface for loading the rule into the database"""
        window = tk.Tk()
        window.title("Load rule")
        
        text_var = tk.StringVar()
        self.rule = {}
        self.value = []
        for row in self.db.select_rules():
            self.rule[row[0]] = row[1]
            self.value.append(row[0])
        self.rule_name = ttk.Combobox(window, textvariable=text_var, values=self.value, state='readonly')
        self.rule_name.grid(row=0, column=1)
        
        self.rule_label = tk.Label(window, text="Rule to load")
        self.rule_label.grid(row=0, column=0)
        
        self.label_code = tk.Label(window, text="Rule code =>")
        self.label_code.grid(row=1, columnspan=2, sticky=tk.W)
        
        self.label_model = tk.Label(window, text="Model =>")
        self.label_model.grid(row=2, columnspan=2, sticky=tk.W)
        
        validate = tk.Button(window, text="Validate")
        validate.grid(row=3, column=1)
    ##################### 
    #        TODO
    #####################
        delete = tk.Button(window, text="Delete")
        delete.grid(row=3, column=0)
    ##################### 
    #        TODO
    #####################
        self.rule_name.bind('<<ComboboxSelected>>', self.on_select) 
        
        
    def on_select(self, event):
        """charge the rule, the code and a model, when the listbox selection is changed"""
        code = self.rule[self.rule_name.get()]
        self.label_code.config(text="Rule code => "  + code)
        self.label_model.config(text="Rule model => " + SINGLE_COR.execute(code))
        
    def del_rule(self, event):
        """delete the rule selected into the combobox from the database"""
        pass   
    ##################### 
    #        TODO
    #####################
    
    def generation_key_window(self):
        """display the choice between load or create rule"""
        window = tk.Tk()
        window.title("Key generation")
        load_rules = tk.Button(window, text="Load a rule", command=self.load_rule) #no command for now
        create_rules = tk.Button(window, text="Create a new rule", command=self.creation_rule) #no command for now
        load_rules.grid(row=0, column=0, sticky=tk.W+tk.E+tk.S+tk.N)
        create_rules.grid(row=1, column=0, sticky=tk.W+tk.E+tk.S+tk.N)
        
        window.mainloop()
        
    def creation_rule(self):
        """window for the creation of a rule"""
        self.window = tk.Tk()
        self.window.title("Rule Creation")
        #code and model
        self._reset_code()
        self.rule = Rules()
        
        #display str
        self.display = 0
        
        #combo Type 
        type_value = ["CODE_STR"]
        type_var = tk.StringVar()
        self.combo_type = ttk.Combobox(self.window, textvariable=type_var, values=type_value, state='readonly')
        self.combo_type.grid(row=0, column=0)
        self.combo_type.current(0)
        self.label_type = tk.Label(self.window, text="Type")
        self.label_type.grid(row = 0, column = 1, sticky=tk.W+tk.E+tk.S+tk.N)
        
        #key length
        var = tk.StringVar(self.window)
        var.set("10")
        self.spin_length = tk.Spinbox(self.window, from_=1, to=MAX_LENGTH, textvariable=var)
        self.spin_length.grid(row=1, column=0, sticky=tk.W+tk.E+tk.S+tk.N)
        self.label_length = tk.Label(self.window, text="Length")
        self.label_length.grid(row=1, column=1)
        
        #text_type
        self.text_type_value = ["CODE_BIN", "CODE_HEXA", "CODE_INT", "CODE_STR"]
        self.text_type_var = tk.StringVar()
        self.combo_text_type = ttk.Combobox(self.window, textvariable=self.text_type_var, values=self.text_type_value, state='readonly')
        self.combo_text_type.grid(row=2, column=0)
        self.combo_text_type.current(2)
        #if function of the current text_type selected, we have different graphical interface
        #same interface for CODE_BIN, CODE_HEXA and CODE_TEXT
        self.combo_text_type.bind('<<ComboboxSelected>>', self.on_select_text_type) 
        self.label_text_type = tk.Label(self.window, text="Text_type")
        self.label_text_type.grid(row=2, column=1)
        
        #readable
        self.check = tk.IntVar()
        self.readable = tk.Checkbutton(self.window, text="Readable key", variable=self.check, command=self.on_check_read)
        
        #combo string value
        self.string_type_value = ["CODE_ASCII", "CODE_STR"]
        self.string_type_var = tk.StringVar()
        self.combo_string_type = ttk.Combobox(self.window, textvariable=self.string_type_var, values=self.string_type_value, state='readonly')
        self.combo_string_type.bind('<<ComboboxSelected>>', self.on_select_text_type)
        self.combo_string_type.current(0)
        self.label_string_type = tk.Label(self.window, text="String_type")
        
        #title part subset
        self.label_subset = tk.Label(self.window, text="Subset\nHow many special char?")
            #capital letter
        self.label_cap = tk.Label(self.window, text="Capital")
        self.cap_length = tk.Spinbox(self.window, from_=0, to=MAX_LENGTH)
            #numbers letter
        self.label_num = tk.Label(self.window, text="Number")
        self.num_length = tk.Spinbox(self.window, from_=0, to=MAX_LENGTH)
            #special char
        self.label_spe_char = tk.Label(self.window, text="Special Char")
        self.spe_char_length = tk.Spinbox(self.window, from_=0, to=MAX_LENGTH)
        
        #code and model
        self.label_code = tk.Label(self.window, text="Rule's code =>" + self.code)
        self.label_model = tk.Label(self.window, text="Rule's model =>" + self.model)
        
        #rule's name
        self.name_rule = tk.Entry(self.window)
        self.label_name = tk.Label(self.window, text="Rule's name")
        
        #validation
        self.validate = tk.Button(self.window, text="Validate")
        
    def on_select_text_type(self, event):
        """this determine the graphical interface in function of the text_type selected"""
        #make the begin of the code
        self.rule.set_type(key_carac_str_to_char(self.combo_type.get()))
        self.rule.set_length(str(self.spin_length.get()))
        self.rule.set_text_type(key_carac_str_to_char(self.combo_text_type.get()))
        
        #if it is CODE_BIN or CODE_HEXA or CODE_INT : there will be the same interface
        if self.combo_text_type.get() in self.text_type_value[:3]:
            self._reset_code()
            self.hide_container()
            
            #create and display the code
            self.code = self.rule.create_code()
            
            #display the rule
            self.model = SINGLE_COR.execute(self.code)
            self._create_model()
        elif self.combo_text_type.get() in self.text_type_value[3:]:
            self._reset_code()
            self.display = 1
            
            #checkbutton readable key
            self.readable.grid(row=3, column=0)
            
            #choice of the string type       
            self.combo_string_type.grid(row=4, column=0) 
            self.label_string_type.grid(row=4, column=1)
            
            #subset part 
            self.label_subset.grid(row=5, columnspan=2)  
            self.label_cap.grid(row=6, column=0) 
            self.cap_length.grid(row=6, column=1)
            self.label_num.grid(row=7, column=0)
            self.num_length.grid(row=7, column=1)
            self.label_spe_char.grid(row=8, column=0)
            self.spe_char_length.grid(row=8, column=1)
            
            #make the code and the model
            if(self.check.get() == 0):
                self.rule.set_readability(key_carac_str_to_char("CODE_READ"))
            else:
                self.rule.set_readability("1")
            self.rule.set_string_type(key_carac_str_to_char(self.combo_string_type.get()))
            self.subset = {}
            self.subset[key_carac_str_to_char("CODE_CAP")] = self.cap_length.get()
            self.subset[key_carac_str_to_char("CODE_INT")] = self.num_length.get()
            self.subset[key_carac_str_to_char("CODE_SPE_CHAR")] = self.spe_char_length.get()
            self.rule. set_spe_char(self.subset)
            self.code = self.rule.create_code()
            self.model = SINGLE_COR.execute(self.code)
            self._create_model()

            
    def _create_model(self):
        """take the information of self.rule and create the code associated"""
        if(self.label_code is not None):
            self.label_code.config(text="Rule's code =>" + self.code)
            self.label_code.grid(row=9, columnspan=2, sticky=tk.W)  
        if(self.label_model is not None):
            self.label_model.config(text="Rule's model =>" + self.model)             
            self.label_model.grid(row=10, columnspan=2, sticky=tk.W)
        self.name_rule.grid(row=11, column=0, sticky=tk.W)
        self.label_name.grid(row=11, column=1, sticky=tk.W)
        self.validate.grid(row=12, columnspan=2)
        
    def _reset_code(self):
        """set the code and the model to "" """
        self.code = ""
        self.model = ""
            
            
    def on_validate_creation(self, event):
        """validate the creation of the rule, verify if the rule exist into the database
        if it already exist, popup appears and ask confirmation for replace, if not the function
        set the new rule into the database"""
        #don't allow empty set
        pass
    #############
    #    TODO
    #############
    
    def on_check_read(self):
        """if the button is check, we add to the list of string_type the value CODE_PASSPHRASE and CODE_4WORD"""
        if(self.check.get() == 0):
            self.string_type_value.append("CODE_PASSPHRASE")
            self.string_type_value.append("CODE_4WORD")
            self.combo_string_type.config(values=self.string_type_value)
            self.check.set(1)
        else:
            self.string_type_value.remove("CODE_PASSPHRASE")
            self.string_type_value.remove("CODE_4WORD")
            self.combo_string_type.config(values=self.string_type_value)
            self.check.set(0)
        
    def hide_container(self):
        """erase of the grid the field for the string generation"""
        if(self.display == 1):
            self.readable.grid_forget()
            self.combo_string_type.grid_forget()
            self.label_string_type.grid_forget()
            self.label_subset.grid_forget()
            self.label_cap.grid_forget()
            self.cap_length.grid_forget()
            self.label_num.grid_forget()
            self.num_length.grid_forget()
            self.label_spe_char.grid_forget()
            self.spe_char_length.grid_forget()
        