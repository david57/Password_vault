"""
*   version 1.0
*   author : david and nadettox
*   desc : graphical interface or key and rules generation
"""

import tkinter as tk
import tkinter.ttk as ttk
from database.database import *
from cor_generator.single_cor import *
from tools.tools import *
from rules_gen.rules_gen import *

MAX_LENGTH = 100000
SPACE = "                                                                           "


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
        self.rule_name.current(0)
        
        self.rule_label = tk.Label(window, text="Rule to load")
        self.rule_label.grid(row=0, column=0)
        
        self.label_code = tk.Label(window, text="Rule code =>")
        self.label_code.grid(row=1, columnspan=2, sticky=tk.W)
        
        self.label_model = tk.Label(window, text="Model =>")
        self.label_model.grid(row=2, columnspan=2, sticky=tk.W)
        
        validate = tk.Button(window, text="Validate", command=self.on_validate_load)
        validate.grid(row=3, column=1)

        delete = tk.Button(window, text="Delete", command=self.on_del_rule)
        delete.grid(row=3, column=0)
        
        self.rule_name.bind('<<ComboboxSelected>>', self.on_select) 
        
    def on_validate_load(self):
        """return the string key generate by the cor_generator"""
        return self.rule_name.get()
        
    
       
    def on_select(self, event):
        """charge the rule, the code and a model, when the listbox selection is changed"""
        code = self.rule[self.rule_name.get()]
        self.label_code.config(text="Rule code => "  + code)
        self.label_model.config(text="Rule model => " + SINGLE_COR.execute(code))
        
    def on_del_rule(self):
        """delete the rule selected into the combobox from the database"""
        self.db.delete_by_code(self.rule[self.rule_name.get()])
        self.value.remove(self.rule_name.get())
        self.rule_name.config(values=self.value)
        self.rule_name.current(0)
    
    def generation_key_window(self):
        """display the choice between load or create rule"""
        window = tk.Tk()
        window.title("Key generation")
        load_rules = tk.Button(window, text="Load a rule", command=self.load_rule) #no command for now
        create_rules = tk.Button(window, text="Create a new rule", command=self.creation_rules_2) #no command for now
        load_rules.grid(row=0, column=0, sticky=tk.W+tk.E+tk.S+tk.N)
        create_rules.grid(row=1, column=0, sticky=tk.W+tk.E+tk.S+tk.N)
        
        window.mainloop()
        
    def _reset_code(self):
        """set the code and the model to "" """
        self.code = ""
        self.model = ""
        
    def creation_rules_2(self):
        """new window for the creation of a rule"""
        self.window = tk.Tk()
        self.window.title("Rule Creation")
        
        #code and model
        self.rule = Rules()
        
        #creation of the notebook
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack()
        self.frame_bin = ttk.Frame(self.notebook)
        self.frame_hexa = ttk.Frame(self.notebook)
        self.frame_int = ttk.Frame(self.notebook)
        self.frame_str = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_bin, text="Binaire")
        self.notebook.add(self.frame_hexa, text="Hexadecimal")
        self.notebook.add(self.frame_int, text="integer")
        self.notebook.add(self.frame_str, text="Textual")
        #creation of frame bin, hexa, int
        self.creation_bin_hexa_int(self.frame_bin, "\nCreation of binary key\n", CODE_BIN)
        self.creation_bin_hexa_int(self.frame_hexa, "\nCreation of hexadecimal key\n", CODE_HEXA)
        self.creation_bin_hexa_int(self.frame_int, "\nCreation of integer key\n", CODE_INT)
        self.creation_str(self.frame_str, "\nCreation of textual key\n")
        
        self.window.mainloop()
        
    def creation_bin_hexa_int(self, frame, label_titre, text_type):
        """frame bin, hexa and int are similar, so we create this with a function"""
        #code and label
        self._reset_code()
        
        #creation of the labelframe
        label_frame = tk.LabelFrame(frame, text=label_titre)
        label_frame.grid(row=0, columnspan=2)
        
        #key length
        var = tk.StringVar(self.window)
        var.set("10")
        self.spin_length = tk.Spinbox(label_frame, from_=1, to=MAX_LENGTH, textvariable=var)
        self.spin_length.grid(row=1, column=1, sticky=tk.W+tk.E+tk.S+tk.N)
        self.label_length = tk.Label(label_frame, text="Length ")
        self.label_length.grid(row=1, column=0)
        
        tk.Label(label_frame, text=SPACE).grid(row=2)
        #button for create a example of your key

        label_model = tk.Label(label_frame, text=self.model, fg='red')
        
        self.button_example = tk.Button(label_frame, text="Show key", command= lambda : self.create_model(label_model, var.get(), text_type))
        self.button_example.grid(row=3, columnspan=2)
        
        #place the label for the model 
        label_model.grid(row=4, columnspan=2)
        
        #place the entry name of the rule
        self.label_name_code_part(frame, 5)
        
        
    
    def label_name_code_part(self, frame, r):
        """create the entry for the name of the future rule
        r is row and c is column or place the entry in function of the frame
        and button for validation"""
        self.label_name_title = tk.Label(frame, text="\nSet the label name of your new rules\n")
        self.label_name_title.grid(row=r, columnspan=2)
        self.label_name = tk.Label(frame, text="Name ")
        self.label_name.grid(row=r+1, column=0)
        self.name_rule = tk.Entry(frame)
        self.name_rule.grid(row=r+1, column=1)
        tk.Label(frame, text=SPACE).grid(row=r+2, columnspan=2)
        self.validation = tk.Button(frame, text="Validation", command=self.on_validate_creation)
        self.validation.grid(row=r+3, columnspan=2)
        
     ##########################################################   
     #TODO : erase redundancy between all create model   
     ##########################################################
       
    def create_model(self, label_model, length, text_type, string_type = CODE_ASCII):
        """create a model for example"""
        self.rule.set_type(CODE_STR) #only CODE_STR for now
        #self.rule.set_length(str(self.spin_length.get()))
        self.rule.set_length(length)
        self.rule.set_text_type(text_type)
        #creation of the code and display
        self.code = self.rule.create_code()
        label_model.config(text="\n" + SINGLE_COR.execute(self.code) + "\n")
    
    def create_model_textual(self, read, label_model, string_type, cap, num, spe):
        """create a textual readable key for example"""
        self.rule.set_type(CODE_STR) #only CODE_STR for now
        self.rule.set_length(str(self.spin_length.get()))
        self.rule.set_text_type(CODE_STR)
        if read :
            self.rule.set_readability(CODE_READ)
        else:
            self.rule.set_readability(CODE_NOT_READ)
        self.rule.set_string_type(string_type)
            #set subset
        self.subset = {}
        self.subset[key_carac_str_to_char("CODE_CAP")] = cap
        self.subset[key_carac_str_to_char("CODE_INT")] = num
        self.subset[key_carac_str_to_char("CODE_SPE_CHAR")] = spe
        self.rule.set_spe_char(self.subset)
            #creation of the code
        self.code = self.rule.create_code()
        #self.model = SINGLE_COR.execute(self.code)
        label_model.config(text="\n" + SINGLE_COR.execute(self.code) + "\n")

        
    def on_validate_creation(self):
        """validate the creation of the rule, verify if the rule exist into the database
        if it already exist, popup appears and ask confirmation for replace, if not the function
        set the new rule into the database"""
        #don't allow empty set
        pass
    #############
    #    TODO
    #############    
        
        
    def creation_str(self, frame, label_titre):    
        """creation of the textual frame"""
        #creation of the label_frame
        label_frame_textual = tk.LabelFrame(frame, text=label_titre)
        label_frame_textual.grid(row=0, columnspan=4)
        
        #key length
        var = tk.StringVar(self.window)
        var.set("10")
        self.spin_length = tk.Spinbox(label_frame_textual, from_=1, to=MAX_LENGTH, textvariable=var)
        self.spin_length.grid(row=0, column=1, sticky=tk.W+tk.E+tk.S+tk.N)
        self.label_length = tk.Label(label_frame_textual, text="Length ")
        self.label_length.grid(row=0, column=0)
        
        #creation of the separator
        separator = tk.Label(label_frame_textual, text=SPACE)
        separator.grid(row=1, columnspan=2)
        
        #creation of the notepad for readable or not readable 
        self.notebook_textual = ttk.Notebook(label_frame_textual)
        self.notebook_textual.grid(row=2, columnspan=2)
        self.frame_read = ttk.Frame(self.notebook_textual)
        self.frame_not_read = ttk.Frame(self.notebook_textual)
        self.notebook_textual.add(self.frame_read, text="Readable")
        self.notebook_textual.add(self.frame_not_read, text="Not Readable")
        
        #label to explain what it is
        label_explain_read = tk.Label(self.frame_read, text="Generation of a readable key\n").grid(row=0, columnspan=4)
        label_explain_not_readable = tk.Label(self.frame_not_read, text="Generation of a random textual key\n").grid(row=0, columnspan=4)
        
        #creation of the radio box for the frame_read and frame_not_read
        v = tk.StringVar()
        v.set(CODE_ASCII)
            # readable
        tk.Radiobutton(self.frame_read, text="ascii", variable=v, value=CODE_ASCII, command=lambda : v.set(CODE_ASCII)).grid(row=1, column=0)
        tk.Radiobutton(self.frame_read, text="string", variable=v, value=CODE_STR, command=lambda : v.set(CODE_STR)).grid(row=1, column=1)
        tk.Radiobutton(self.frame_read, text="4word", variable=v, value=CODE_4WORD, command=lambda : v.set(CODE_4WORD)).grid(row=1, column=2) 
        tk.Radiobutton(self.frame_read, text="passphrase", variable=v, value=CODE_PASSPHRASE, command=lambda : v.set(CODE_PASSPHRASE)).grid(row=1, column=3) 
            #not readable
        tk.Radiobutton(self.frame_not_read, text="ascii", variable=v, value=CODE_ASCII, command=lambda : v.set(CODE_ASCII)).grid(row=1, column=0)
        tk.Radiobutton(self.frame_not_read, text="string", variable=v, value=CODE_STR, command=lambda : v.set(CODE_STR)).grid(row=1, column=1)
        
        #creation of the special char field
         #title part subset
        for fr in [self.frame_read, self.frame_not_read]:
            self.label_subset = tk.Label(fr, text="\nHow many special char?\n").grid(row=2, columnspan=2)
            self.label_cap = tk.Label(fr, text="Capital").grid(row=3, column=0)
            self.label_num = tk.Label(fr, text="Number").grid(row=4, column=0)
            self.label_spe_char = tk.Label(fr, text="Special Char").grid(row=5, column=0)
            tk.Label(fr, text=SPACE).grid(row=6, columnspan=2)
        var_cap = tk.StringVar(fr)
        var_num = tk.StringVar(fr)
        var_spe = tk.StringVar(fr)
        var_cap.set("0")
        var_num.set("0")
        var_spe.set("0")
            #capital letter
        self.cap_length = tk.Spinbox(self.frame_read, from_=0, to=MAX_LENGTH, textvariable=var_cap).grid(row=3, column=1)
        self.cap_length = tk.Spinbox(self.frame_not_read, from_=0, to=MAX_LENGTH, textvariable=var_cap).grid(row=3, column=1)
            #numbers letter
        self.num_length = tk.Spinbox(self.frame_read, from_=0, to=MAX_LENGTH, textvariable=var_num).grid(row=4, column=1)
        self.num_length = tk.Spinbox(self.frame_not_read, from_=0, to=MAX_LENGTH, textvariable=var_num).grid(row=4, column=1)
            #special char
        self.spe_char_length = tk.Spinbox(self.frame_read, from_=0, to=MAX_LENGTH, textvariable=var_spe).grid(row=5, column=1)
        self.spe_char_length = tk.Spinbox(self.frame_not_read, from_=0, to=MAX_LENGTH, textvariable=var_spe).grid(row=5, column=1)
        
        #creation of button for show the example
        tk.Button(self.frame_read, text="Show key", command= lambda : self.create_model_textual(True, label_model_read, v.get(), var_cap.get(), var_num.get(), var_spe.get())).grid(row=7, columnspan=2)
        tk.Button(self.frame_not_read, text="Show key", command= lambda : self.create_model_textual(False, label_model_not_read, v.get(), var_cap.get(), var_num.get(), var_spe.get())).grid(row=7, columnspan=2)
        
        #creation of label_model
        label_model_read = tk.Label(self.frame_read, text=self.model, fg='red')
        label_model_read.grid(row=8, columnspan = 4)
        label_model_not_read = tk.Label(self.frame_not_read, text=self.model, fg='red')
        label_model_not_read.grid(row=8, columnspan = 4)
        
        #place the entry name of the rule
        self.label_name_code_part(frame, 1)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  